from copy import deepcopy

f = open("../input/24", "r")
data = [line.rstrip('\n') for line in f]
f.close()

ADJACENT_POSITIONS = [(1,0), (-1,0), (0,1), (0,-1)]

def get_adjacent(pos):
    return [(pos[0]+y, pos[1]+x) for y, x in ADJACENT_POSITIONS]


def print_state(state):
    for row in range(len(state)):
        for col in range(len(state[row])):
            print(state[row][col], end="")
        print("")
    print("")


def living_neighbours(state, pos, level=None, part=1):
    living_neighbours = 0
    if part == 1:
        adj = get_adjacent(pos)
        for p in adj:
            if p[0] >= 0 and p[1] >= 0 and \
                p[0] <= 4 and p[1] <= 4 and \
                state[p[0]][p[1]] == "#":
                living_neighbours += 1

    if part == 2:
        row, col = pos
        neighbours = [state[level][row+y][col+x]
                for y, x in ADJACENT_POSITIONS
                if 0 <= row+y < len(state[level]) and
                0 <= col+x < len(state[level][0])]

        if row == 0:
            neighbours.append(state[level-1][1][2])
        if row == 4:
            neighbours.append(state[level-1][3][2])
        if col == 0:
            neighbours.append(state[level-1][2][1])
        if col == 4:
            neighbours.append(state[level-1][2][3])

        if (row, col) == (1, 2):
            neighbours.extend(state[level+1][0])
        if (row, col) == (3, 2):
            neighbours.extend(state[level+1][-1])
        if (row, col) == (2, 1):
            neighbours.extend(state[level+1][row][0] for row in range(5))
        if (row, col) == (2, 3):
            neighbours.extend(state[level+1][row][-1] for row in range(5))

        living_neighbours = neighbours.count("#")

    return living_neighbours


def do_tick(state):
    new_state = [["."]*5 for _ in range(5)]

    for y in range(5):
        for x in range(5):
            bugs_nearby = living_neighbours(state, (y, x))
            if state[y][x] == "#":
                if bugs_nearby == 1:
                    new_state[y][x] = "#"
            elif state[y][x] == ".":
                if bugs_nearby == 1 or bugs_nearby == 2:
                    new_state[y][x] = "#"

    return new_state


def biodiversity(state):
    res = 0
    p = 1

    for y in range(5):
        for x in range(5):
            if state[y][x] == "#":
                res += p
            p *= 2
    return res


def solve_part_one():
    state = data[:]
    seen = set()

    while biodiversity(state) not in seen:
        seen.add(biodiversity(state))
        state = do_tick(state)

    return biodiversity(state)


def solve_part_two():
    state = []

    for row in data:
        state.append(list(row))

    state[2][2] = "."

    states = [[["."] * 5 for _ in range(5)] for _ in range(250)]
    states[0] = state

    for minute in range(200):
        new_states = states[:]

        for level in range(-minute-1, minute+2):
            new_level = deepcopy(states[level])
            for row in range(5):
                for col in range(5):
                    if (row, col) == (2, 2):
                        continue

                    curr = states[level][row][col]
                    bugs_nearby = living_neighbours(states, (row, col), level, 2)

                    if curr == "#":
                        if bugs_nearby == 1:
                            pass
                        else:
                            new_level[row][col] = "."
                    else:
                        if bugs_nearby == 1 or bugs_nearby == 2:
                            new_level[row][col] = "#"

            new_states[level] = new_level
        states = new_states
    return sum(sum(row.count("#") for row in state) for state in states)


if __name__ == '__main__':
    print("p1:", solve_part_one())
    print("p2:", solve_part_two())
