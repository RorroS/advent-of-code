from collections import deque

f = open("../input/23", "r")
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


def solve(part=1):
    programs = [Program(intcode_program[:]) for _ in range(50)]
    qs = [deque() for _ in range(50)]

    if part == 2:
        nat = None
        prev_y = None

    for i in range(50):
        out = programs[i].run(i)
        for addr, x, y in list(zip(*[iter(out)]*3)):
            if addr == 255:
                if part == 1:
                    return y
                elif part == 2:
                    nat = (x, y)
            else:
                qs[addr].append((x, y))

    while True:
        if part == 2:
            idle = [False for _ in range(50)]

        for i in range(50):
            if qs[i]:
                inp = list(qs[i].popleft())
            else:
                inp = [-1]
                if part == 2:
                    idle[i] = True

            out = programs[i].run_many(inp)
            for addr, x, y in list(zip(*[iter(out)]*3)):
                if addr == 255:
                    if part == 1:
                        return y
                    elif part == 2:
                        nat = (x, y)
                else:
                    qs[addr].append((x, y))

        if part == 2 and all(idle):
            qs[0].append(nat)
            if nat[1] == prev_y:
                return nat[1]
            else:
                prev_y = nat[1]


if __name__ == '__main__':
    print("p1:", solve())
    print("p2:", solve(2))

