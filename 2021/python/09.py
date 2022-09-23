import math

with open('../input/09') as f:
    heatmap = [[int(x) for x in line.rstrip()] for line in f]


def get_adjacent(x, y, heatmap):
    adjacent = []
    if (x < len(heatmap[0])-1):
        adjacent.append(heatmap[y][x+1])  # right neighbour
    if (y < len(heatmap)-1):
        adjacent.append(heatmap[y+1][x])  # bottom neighbour
    if (x-1 >= 0):
        adjacent.append(heatmap[y][x-1])  # left neighbour
    if (y-1 >= 0):
        adjacent.append(heatmap[y-1][x])  # top neighbour

    return adjacent


def solve_part_one():
    low_points = []
    for y in range(len(heatmap)):
        for x in range(len(heatmap[0])):
            adjacent = get_adjacent(x, y, heatmap)
            if not any([n <= heatmap[y][x] for n in adjacent]):
                low_points.append(heatmap[y][x] + 1)
    return sum(low_points)


basin_groups = []  # too lazy to do it in a better way


def count_basin(x, y):
    if x < 0 or x >= len(heatmap[0]) or y < 0 or y >= len(heatmap) or heatmap[y][x] == 9 or heatmap[y][x] == -1:
        return

    heatmap[y][x] = -1
    basin_groups[len(basin_groups)-1] += 1
    count_basin(x+1, y)
    count_basin(x-1, y)
    count_basin(x, y+1)
    count_basin(x, y-1)


def solve_part_two():
    for y in range(len(heatmap)):
        for x in range(len(heatmap[0])):
            basin_groups.append(0)
            count_basin(x, y)

    return math.prod(sorted(basin_groups)[-3:])


if __name__ == '__main__':
    print('p1:', solve_part_one())
    print('p2:', solve_part_two())
