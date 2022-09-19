with open('../input/05', 'r') as f:
    coordinates = [line.rstrip().replace(' -> ', ',')
                   for line in f.readlines()]


def solve_part_one():
    all_points = dict()

    for coord in coordinates:
        x1, y1, x2, y2 = map(int, coord.split(","))

        if x1 == x2 or y1 == y2:
            for i in range(min(x1, x2), max(x1, x2) + 1):
                for j in range(min(y1, y2), max(y1, y2) + 1):
                    if (i, j) not in all_points:
                        all_points[(i, j)] = 1
                    else:
                        all_points[(i, j)] += 1

    dupes = 0
    for p in all_points:
        dupes += all_points[p] > 1

    return dupes


def solve_part_two():
    all_points = dict()

    for coord in coordinates:
        x1, y1, x2, y2 = map(int, coord.split(","))

        if x1 == x2 or y1 == y2:
            for i in range(min(x1, x2), max(x1, x2) + 1):
                for j in range(min(y1, y2), max(y1, y2) + 1):
                    if (i, j) not in all_points:
                        all_points[(i, j)] = 1
                    else:
                        all_points[(i, j)] += 1
        else:
            x_direction = 1 if x1 < x2 else -1  # 1 going right, -1 going left
            y_direction = 1 if y1 < y2 else -1  # 1 going down, -1 going up
            y = y1
            for x in range(x1, x2 + x_direction, x_direction):
                if (x, y) not in all_points:
                    all_points[(x, y)] = 1
                else:
                    all_points[(x, y)] += 1

                y += y_direction

    dupes = 0
    for p in all_points:
        dupes += all_points[p] > 1

    return dupes


if __name__ == '__main__':
    print("p1:", solve_part_one())
    print("p2:", solve_part_two())
