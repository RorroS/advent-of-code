import copy

f = open("../input/11", "r")
one_per_line = [[ch for ch in line.rstrip('\n')] for line in f]
f.close()

FLOOR = "."
EMPTY = "L"
OCCUPIED = "#"
debug_p1 = False
debug_p2 = False

def get_neighbours_p1(layout, y, x):
    neighbours = []

    possible_neighbours = [
        (y-1, x-1), (y-1, x),   (y-1, x+1),
        (y, x-1),               (y, x+1),
        (y+1, x-1), (y+1, x),   (y+1, x+1)
    ]

    for row, col in possible_neighbours:
        if row >= 0 and row < len(layout) and \
            col >= 0 and col < len(layout[0]):
                neighbours.append((row, col))

    return neighbours


def solve_part_one():
    changed = True
    current_layout = copy.deepcopy(one_per_line)

    while changed:
        temp_layout = copy.deepcopy(current_layout)

        if debug_p1:
            for line in current_layout:
                for seat in line:
                    print(seat, end = "")
                print()
            print()

        changed = False
        for i in range(len(one_per_line)):
            for j in range(len(one_per_line[i])):
                if current_layout[i][j] != FLOOR:
                    neighbours = get_neighbours_p1(current_layout, i, j)
                    occupied_neighbours = 0
                    for row, col in neighbours:
                        if current_layout[row][col] == OCCUPIED:
                            occupied_neighbours += 1

                    if current_layout[i][j] == EMPTY:
                        if not occupied_neighbours:
                            temp_layout[i][j] = OCCUPIED
                            changed = True
                    else:
                        if occupied_neighbours >= 4:
                            temp_layout[i][j] = EMPTY
                            changed = True

        current_layout = copy.deepcopy(temp_layout)

    occupied_seats = 0
    for i in range(len(one_per_line)):
        for j in range(len(one_per_line[i])):
            if current_layout[i][j] == OCCUPIED:
                occupied_seats += 1

    return occupied_seats


def get_neighbours_p2(layout, y, x):
    neighbours = []

    # up left
    for i in range(1, len(layout) + len(layout[0])):
        if (y - i) >= 0 and (x - i) >= 0 and layout[y - i][x - i] != FLOOR:
            neighbours.append((y - i, x - i))
            break

    # up
    for i in range(1, len(layout)):
        if (y - i) >= 0 and layout[y - i][x] != FLOOR:
            neighbours.append((y - i, x))
            break

    # up right
    for i in range(1, len(layout[0])):
        if (y - i) >= 0 and (x + i) < len(layout[0]) and layout[y - i][x + i] != FLOOR:
            neighbours.append((y - i, x + i))
            break

    # left
    for i in range(1, len(layout[0])):
        if (x - i) >= 0 and layout[y][x - i] != FLOOR:
            neighbours.append((y, x - i))
            break

    # right
    for i in range(1, len(layout[0])):
        if (x + i) < len(layout[0]) and layout[y][x + i] != FLOOR:
            neighbours.append((y, x + i))
            break

    # down left
    for i in range(1, len(layout)):
        if (y + i) < len(layout) and (x - i) >= 0 and layout[y + i][x - i] != FLOOR:
            neighbours.append((y + i, x - i))
            break

    # down
    for i in range(1, len(layout)):
        if (y + i) < len(layout) and layout[y + i][x] != FLOOR:
            neighbours.append((y + i, x))
            break

    # down right
    for i in range(1, len(layout) + len(layout[0])):
        if (y + i) < len(layout) and (x + i) < len(layout[0]) and layout[y + i][x + i] != FLOOR:
            neighbours.append((y + i, x + i))
            break

    return neighbours


def solve_part_two():
    changed = True
    current_layout = copy.deepcopy(one_per_line)

    while changed:
        temp_layout = copy.deepcopy(current_layout)

        if debug_p2:
            for line in current_layout:
                for seat in line:
                    print(seat, end = "")
                print()
            print()

        changed = False
        for i in range(len(one_per_line)):
            for j in range(len(one_per_line[i])):
                neighbours = get_neighbours_p2(current_layout, i, j)
                occupied_neighbours = 0
                for row, col in neighbours:
                    if current_layout[row][col] == OCCUPIED:
                        occupied_neighbours += 1

                if current_layout[i][j] == EMPTY:
                    if not occupied_neighbours:
                        temp_layout[i][j] = OCCUPIED
                        changed = True
                elif current_layout[i][j] == OCCUPIED:
                    if occupied_neighbours >= 5:
                        temp_layout[i][j] = EMPTY
                        changed = True

        current_layout = copy.deepcopy(temp_layout)

    occupied_seats = 0
    for i in range(len(one_per_line)):
        for j in range(len(one_per_line[i])):
            if current_layout[i][j] == OCCUPIED:
                occupied_seats += 1

    return occupied_seats


if __name__ == '__main__':
    print("p1:", solve_part_one())
    print("p2:", solve_part_two())

