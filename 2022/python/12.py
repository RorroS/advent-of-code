with open('../input/12') as f:
    grid = [[ch for ch in line.rstrip()] for line in f]

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1]]
WIDTH = len(grid[0])
HEIGHT = len(grid)


def elevation(ch) -> int:
    if (ch == 'S'):
        return elevation('a')
    elif (ch == 'E'):
        return elevation('z')
    else:
        return ALPHABET.index(ch)


def find_start_end() -> list[tuple[int, int]]:
    start = (0, 0)
    end = (0, 0)
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 'S':
                start = (y, x)
            elif grid[y][x] == 'E':
                end = (y, x)

    return [start, end]


def get_neighbours(y: int, x: int, backwards: bool) -> list[tuple[int, int]]:
    neighbours = []

    for dy, dx in DIRECTIONS:
        ny = y + dy
        nx = x + dx

        if not (0 <= ny < HEIGHT and 0 <= nx < WIDTH):
            continue

        if (elevation(grid[ny][nx]) <= elevation(grid[y][x]) + 1) if not backwards else (elevation(grid[ny][nx]) >= elevation(grid[y][x]) - 1):
            neighbours.append((ny, nx))
    return neighbours


# https://en.wikipedia.org/wiki/Dijkstras_algorithm
def dijkstra(grid: list[list[str]], start: tuple[int, int], end: tuple[int, int], backwards: bool = False) -> int | None:
    visited = [[False for ch in l] for l in grid]
    queue: list[tuple[int, int, int]] = [(0, *start)]

    while len(queue) > 0:
        steps, curr_y, curr_x = queue[0]
        queue = queue[1:]

        if (visited[curr_y][curr_x]):
            continue

        visited[curr_y][curr_x] = True

        if ((curr_y, curr_x) == end) if not backwards else (elevation(grid[curr_y][curr_x]) == 0):
            return steps

        neighbours = get_neighbours(curr_y, curr_x, backwards)
        for ny, nx in neighbours:
            queue.append((steps + 1, ny, nx))


def solve_part_one(start: tuple[int, int], end: tuple[int, int]) -> int | None:
    return dijkstra(grid, start, end)


def solve_part_two(start: tuple[int, int], end: tuple[int, int]) -> int | None:
    return dijkstra(grid, end, start, True)


if __name__ == '__main__':
    start, end = find_start_end()
    print('p1: ', solve_part_one(start, end))
    print('p2: ', solve_part_two(start, end))
