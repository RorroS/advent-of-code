f = open("../input/15", "r")
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
WALL = 0
EMPTY = 1
OXYGEN = 2

NORTH = 1
SOUTH = 2
WEST = 3
EAST = 4

UP = (-1, 0)
DOWN = (1, 0)
RIGHT = (0, 1)
LEFT = (0, -1)

ADJACENT_POSITIONS = [UP, DOWN, LEFT, RIGHT]
DIRECTIONS = {NORTH: UP, SOUTH: DOWN, EAST: RIGHT, WEST: LEFT}
REVERSE_DIRECTIONS = {NORTH: SOUTH, SOUTH: NORTH, EAST: WEST, WEST: EAST}


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

    def run(self, u_in = None):
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
                dest = self.get_real_index(0, mode)

                if u_in is None:
                    return None
                self.code[dest] = u_in
                u_in = None
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
                self.halted = True
                return None


def dfs(curr_pos, grid, target, prog):
    for d, pos in DIRECTIONS.items():
        new_pos = (curr_pos[0] + pos[0], curr_pos[1] + pos[1])

        if new_pos not in grid:
            out = prog.run(d)
            grid[new_pos] = out

            if out != WALL:
                curr_pos = new_pos

                if out == OXYGEN:
                    target = curr_pos

                curr_pos, grid, target = dfs(curr_pos, grid, target, prog)

                reverse_d = REVERSE_DIRECTIONS[d]
                reverse_pos = DIRECTIONS[reverse_d]
                out = prog.run(reverse_d)
                curr_pos = (curr_pos[0] + reverse_pos[0], curr_pos[1] + reverse_pos[1])

    return curr_pos, grid, target


def bfs(from_node, get_positions):
    vals = {from_node: 0}
    to_search = [from_node]
    dist = 0

    while to_search:
        new_to_search = []
        dist += 1
        for pos in to_search:
            for new_pos in get_positions(pos):
                if new_pos not in vals:
                    new_to_search.append(new_pos)
                    vals[new_pos] = dist

        to_search = new_to_search

    return vals

def solve():
    prog = Program(intcode_program)

    curr_pos = (0, 0)

    grid = {}
    grid[curr_pos] = EMPTY

    oxygen_pos = None

    curr_pos, grid, oxygen_pos = dfs(curr_pos, grid, oxygen_pos, prog)

    def get_positions(pos):
        adjacent = []
        y, x = pos
        for dy, dx in ADJACENT_POSITIONS:
            new_y = y + dy
            new_x = x + dx
            new_pos = (new_y, new_x)

            if grid[new_pos] != WALL:
                adjacent.append(new_pos)

        return adjacent

    vals = bfs((0,0), get_positions)
    if oxygen_pos not in vals:
        print("Didn't find shit...")
        return

    p1 = vals[oxygen_pos]

    print("p1:", p1)

    vals = bfs(oxygen_pos, get_positions)
    print("p2:", max(vals.values()))


if __name__ == '__main__':
    solve()
