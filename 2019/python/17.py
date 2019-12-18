f = open("../input/17", "r")
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
DIRECTIONS = {94: "^", 118: "v", 60: "<", 62: ">"}
UP = 94
DOWN = 118
LEFT = 60
RIGHT = 62

# Manual labour
MAIN = "A,B,A,B,C,C,B,A,C,A"
A = "L,10,R,8,R,6,R,10"
B = "L,12,R,8,L,12"
C = "L,10,R,8,R,8"
END_PROGRAM = "n"


class Program:
    def __init__(self, code, u_in):
        self.code = code
        self.curr_index = 0
        self.relative_base = 0
        self.halted = False
        self.input = u_in


    def get_real_index(self, i, mode):
        mode = (POSITION_MODE if i >= len(mode) else mode[i])
        val = self.code[self.curr_index+1+i]
        if mode == POSITION_MODE:
            pass
        elif mode == RELATIVE_MODE:
            val = val+self.relative_base
        else:
            assert False
        while len(self.code)-1 <= val:
            self.code.append(0)
        return val


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


    def run(self, u_in = None):
        while True:
            command = self.code[self.curr_index]
            opcode, mode = self.get_opcode_mode(command)

            if opcode == ADD:
                val1 = self.get_real_value(0, mode)
                val2 = self.get_real_value(1, mode)
                dest = self.get_real_index(2, mode)

                self.code[dest] = val1 + val2
                self.curr_index += 4

            elif opcode == MUL:
                val1 = self.get_real_value(0, mode)
                val2 = self.get_real_value(1, mode)
                dest = self.get_real_index(2, mode)

                self.code[dest] = val1 * val2
                self.curr_index += 4

            elif opcode == IN:
                dest = self.get_real_index(0, mode)

                self.code[dest] = self.input[0]
                self.input.pop(0)

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

                if val1 < val2:
                    self.code[dest] = 1
                else:
                    self.code[dest] = 0
                self.curr_index += 4

            elif opcode == EQUALS:
                val1 = self.get_real_value(0, mode)
                val2 = self.get_real_value(1, mode)
                dest = self.get_real_index(2, mode)

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
                self.halted = True
                return None


def print_grid(grid):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 35: # scaffolding
                print("¤", end="")
            elif grid[y][x] == 46:
                print(".", end="")
            if grid[y][x] in [UP, DOWN, LEFT, RIGHT]:
                print(DIRECTIONS[grid[y][x]], end="")
        print("")


def get_ascii(func):
    res = []
    for ch in func:
        res.append(ord(ch))
    return res


def get_grid(print_g = False):
    prog = intcode_program[:]
    program = Program(prog, [])
    grid = []
    curr = []
    while True:
        res = program.run()
        if res == None:
            break
        if res == 10:
            grid.append(curr)
            curr = []
        else:
            curr.append(res)
            continue
    if print_g:
        print_grid(grid)

    return grid


def solve_part_one():
    grid = get_grid()
    tot = 0
    for x in range(1, len(grid)-2):
        for y in range(1, len(grid[0])-1):
            if grid[x][y] != 35:
                continue
            if grid[x-1][y] == grid[x+1][y] == grid[x][y-1] == grid[x][y+1]:
                tot += x*y
    return tot


def solve_part_two():
    ascii_prog = get_ascii(MAIN)+[ord("\n")] + get_ascii(A)+[ord("\n")] + \
            get_ascii(B) + [ord("\n")] + get_ascii(C) + [ord("\n")] + \
            get_ascii(END_PROGRAM) + [ord("\n")]

    program = Program(intcode_program, ascii_prog)
    program.code[0] = 2

    while True:
        res = program.run()
        if res == None:
            break
        if res > 255:
            return res


if __name__ == '__main__':
    print("p1:",solve_part_one())
    print("p2:",solve_part_two())
