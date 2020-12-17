with open("../input/17", "r") as f:
    inp = [[r for r in row] for row in f.read().rstrip().split("\n")]


def init_cubes(grid, part_two):
    active_cubes = set()
    height = len(inp)
    width = len(inp[0])

    for y in range(height):
        for x in range(width):
            if grid[y][x] == "#":
                if part_two:
                    active_cubes.add((x, y, 0, 0))
                else:
                    active_cubes.add((x, y, 0))

    return active_cubes


def get_neighbours(coords):
    neighbours = []
    possibilities = [-1, 0, 1]

    for nx in possibilities:
        for ny in possibilities:
            for nz in possibilities:
                if len(coords) == 4:
                    x, y, z, w = coords

                    for nw in possibilities:
                        if nx != 0 or ny != 0 or nz != 0 or nw != 0:
                            neighbours.append((x+nx, y+ny, z+nz, w+nw))
                else:
                    x, y, z = coords
                    if nx != 0 or ny != 0 or nz != 0:
                        neighbours.append((x+nx, y+ny, z+nz))


    return neighbours


def count_neighbours(active_cubes, coords):
    cnt = 0
    for neighbour in get_neighbours(coords):
        if neighbour in active_cubes:
            cnt += 1
    return cnt


def do(active_cubes):
    temp_active_cubes = set()

    for coords in active_cubes:
        if count_neighbours(active_cubes, coords) in [2,3]:
            temp_active_cubes.add(coords)

        for n_coords in get_neighbours(coords):
            if n_coords not in active_cubes and count_neighbours(active_cubes, n_coords) == 3:
                temp_active_cubes.add(n_coords)

    return temp_active_cubes


def solve_part_one():
    active_cubes = init_cubes(inp, False)
    for _ in range(6):
        active_cubes = do(active_cubes)

    return len(active_cubes)


def solve_part_two():
    active_cubes = init_cubes(inp, True)
    for _ in range(6):
        active_cubes = do(active_cubes)

    return len(active_cubes)


if __name__ == '__main__':
    print("p1:", solve_part_one())
    print("p2:", solve_part_two())
