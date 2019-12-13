f = open("../input/13", "r")
intcode_program = [int(num) for num in f.read().rstrip().split(',')]
f.close()

# Variables for the intcode program
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

# Variables for today's puzzle
EMPTY = 0
WALL = 1
BLOCK = 2
PADDLE = 3
BALL = 4


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

    def add_input(self, u_in):
        self.input.append(u_in)
        print("Current input:", len(self.input))

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

def solve_part_one():
    num_blocks = 0
    program = Program(intcode_program, (lambda: 0))
    grid = {}

    while True:
        xcord = program.run()
        ycord = program.run()
        tile_id = program.run()

        if xcord == None or ycord == None or tile_id == None:
            break
        grid[(xcord, ycord)] = tile_id

    for pos in grid:
        if grid[pos] == BLOCK:
            num_blocks += 1

    assert num_blocks == 205
    print("p1:", num_blocks)


def solve_part_two():
    def get_input():
        if ball_x < paddle_x:
            return -1
        elif ball_x > paddle_x:
            return 1
        else:
            return 0

    code = intcode_program[:]
    code[0] = 2
    program = Program(code, get_input)
    grid = {}

    ball_x = 0
    paddle_x = 0
    score = 0

    while True:
        xcord = program.run()
        ycord = program.run()
        tile_id = program.run()

        if xcord == None or ycord == None or tile_id == None:
            break

        if xcord == -1 and ycord == 0:
            score = tile_id

        if tile_id == BALL:
            ball_x = xcord
        elif tile_id == PADDLE:
            paddle_x = xcord

        grid[(xcord, ycord)] = tile_id
    print("p2:", score)


if __name__ == '__main__':
    solve_part_one()
    solve_part_two()
