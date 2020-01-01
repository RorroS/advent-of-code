f = open("../input/25", "r")
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

# Change to False to play manually
AUTO = True

class Program:
    def __init__(self, code):
        self.code = code
        self.curr_index = 0
        self.relative_base = 0
        self.halted = False


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

    def run_many(self, inp):
        out = []
        for i in inp:
            output = self.run(i)
            out += output
            if self.halted:
                break
        return out

    def run(self, inp = None):
        out = []
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
                if inp is None:
                    return out

                dest = self.get_real_index(0, mode)
                self.code[dest] = inp
                inp = None
                self.curr_index += 2

            elif opcode == OUT:
                val1 = self.get_real_value(0, mode)
                out.append(val1)
                self.curr_index += 2

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
                return out

def print_output(out):
    for ch in out:
        if ch <= 127:
            print(chr(ch), end="")

def manual(prog):
    print_output(prog.run())

    while True:
        inp = input("?: ")
        inp = [ord(c) for c in inp] + [ord("\n")]
        out = prog.run_many(inp)

        print_output(out)

def automatic(prog):
    commands = [
    "south",
    "take fuel cell",
    "north",
    "west",
    "take mutex",
    "south",
    "south",
    "take coin",
    "north",
    "east",
    "take cake",
    "north",
    "west",
    "south",
    "west"
    ]

    for com in commands:
        inp = [ord(c) for c in com] + [ord("\n")]
        out = prog.run_many(inp)

    print_output(out)

def solve_part_one():
    code = intcode_program[:]
    prog = Program(intcode_program)

    if AUTO:
        automatic(prog)
    else:
        manual(prog)

if __name__ == '__main__':
    solve_part_one()
