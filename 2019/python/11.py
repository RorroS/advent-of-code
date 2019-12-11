from collections import defaultdict
f = open("../input/11", "r")
intcode_program = [int(num) for num in f.read().rstrip().split(',')]
f.close()

ADD = 1
MUL = 2
IN = 3
OUT = 4
JMP_IF_TRUE = 5
JMP_IF_FALSE = 6
LESS_THAN = 7
EQUALS = 8
RELATIVE_BASE = 9
TERMINATE = 99

POSITION_MODE = 0
IMMEDIATE_MODE = 1
RELATIVE_MODE = 2

BLACK = 0
WHITE = 1
LEFT = 0
RIGHT = 1

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3


class Program:
    def __init__(self, code, u_input):
        self.code = code
        self.input = u_input
        self.curr_index = 0
        self.relative_base = 0


    def get_real_index(self, i, mode):
        mode = (POSITION_MODE if i >= len(mode) else mode[i])
        val = self.code[self.curr_index+1+i]
        if mode == POSITION_MODE:
            return val
        elif mode == RELATIVE_MODE:
            return val+self.relative_base
        else:
            assert False


    def get_real_value(self, i, mode):
        mode = (POSITION_MODE if i >= len(mode) else mode[i])
        val = self.code[self.curr_index+1+i]
        if mode == POSITION_MODE:
            while len(self.code) <= val:
                self.code.append(0)
            val = self.code[val]
        elif mode == RELATIVE_MODE:
            val = self.code[val+self.relative_base]
        return val


    def get_opcode_mode(self, command):
        opcode = command%100
        all_modes = str(command//100)[::-1]

        mode = []
        for m in all_modes:
            mode.append(int(m))
        return opcode, mode


    def run(self):
        while True:
            command = self.code[self.curr_index]
            opcode, mode = self.get_opcode_mode(command)

            if opcode == ADD:
                val1 = self.get_real_value(0, mode)
                val2 = self.get_real_value(1, mode)
                dest = self.get_real_index(2, mode)

                while len(self.code) <= dest:
                    self.code.append(0)

                self.code[dest] = val1 + val2
                self.curr_index += 4

            elif opcode == MUL:
                val1 = self.get_real_value(0, mode)
                val2 = self.get_real_value(1, mode)
                dest = self.get_real_index(2, mode)

                while len(self.code) <= dest:
                    self.code.append(0)

                self.code[dest] = val1 * val2
                self.curr_index += 4

            elif opcode == IN:
                u_in = self.input
                dest = self.get_real_index(0, mode)

                self.code[dest] = u_in()
                self.curr_index += 2

            elif opcode == OUT:
                val1 = self.get_real_value(0, mode)

                self.curr_index += 2
                return val1

            elif opcode == JMP_IF_TRUE:
                val1 = self.get_real_value(0, mode)
                val2 = self.get_real_value(1, mode)

                if val1 != 0:
                    self.curr_index = val2
                else:
                    self.curr_index += 3

            elif opcode == JMP_IF_FALSE:
                val1 = self.get_real_value(0, mode)
                val2 = self.get_real_value(1, mode)

                if val1 == 0:
                    self.curr_index = val2
                else:
                    self.curr_index += 3

            elif opcode == LESS_THAN:
                val1 = self.get_real_value(0, mode)
                val2 = self.get_real_value(1, mode)
                dest = self.get_real_index(2, mode)

                while len(self.code) <= dest:
                    self.code.append(0)

                if val1 < val2:
                    self.code[dest] = 1
                else:
                    self.code[dest] = 0
                self.curr_index += 4

            elif opcode == EQUALS:
                val1 = self.get_real_value(0, mode)
                val2 = self.get_real_value(1, mode)
                dest = self.get_real_index(2, mode)

                while len(self.code) <= dest:
                    self.code.append(0)

                if val1 == val2:
                    self.code[dest] = 1
                else:
                    self.code[dest] = 0
                self.curr_index += 4

            elif opcode == RELATIVE_BASE:
                val1 = self.get_real_value(0, mode)

                self.relative_base += val1
                self.curr_index += 2

            elif opcode == TERMINATE:
                return None


def make_grid(rows, columns):
    grid = []
    for _ in range(rows):
        row = []
        for _ in range(columns):
            row.append(0)
        grid.append(row)
    return grid


def get_dir(curr_dir, turn):
    new_dir = 0
    if turn == 0:
        new_dir = curr_dir + 1
    else:
        new_dir = curr_dir - 1
    return new_dir%4


def get_pos(row, col, direction):
    if direction == UP:
        return row-1, col
    elif direction == RIGHT:
        return row, col+1
    elif direction == DOWN:
        return row+1, col
    else:
        return row, col-1


def solve(part):
    ROWS = 69 if part == 1 else 11
    COLUMNS = 137 if part == 1 else 80
    grid = make_grid(ROWS, COLUMNS)
    curr_row, curr_col = ROWS//2, COLUMNS//2
    grid[curr_row][curr_col] = 1 if part == 2 else 0
    direction = UP

    def get_color():
        return grid[curr_row][curr_col]

    painted = []
    program = Program(intcode_program, get_color)

    while True:
        color = program.run()

        if color == None:
            break

        grid[curr_row][curr_col] = color

        if (curr_row, curr_col) not in painted:
            painted.append((curr_row, curr_col))
        turn = program.run()
        direction = get_dir(direction, turn)
        curr_row, curr_col = get_pos(curr_row, curr_col, direction)

    if part == 1:
        return len(painted)
    else:
        return grid, ROWS, COLUMNS


def solve_part_one():
    result = solve(1)
    assert result == 2478, "expected 2478, got " + result
    return result


def solve_part_two():
    grid, ROWS, COLUMNS = solve(2)
    print("p2:")
    output = []
    for row in range(ROWS):
        row_str = ""
        for col in range(COLUMNS):
            row_str += "#" if grid[row][COLUMNS-col-40] == 1 else " "
        if "#" in row_str:
            output.append(row_str)

    for line in output:
        print(line)


if __name__ == '__main__':
    print("p1:", solve_part_one())
    solve_part_two()

