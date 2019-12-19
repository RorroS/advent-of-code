import time
from collections import deque

f = open("../input/18", "r")
data = [line.rstrip('\n') for line in f]
f.close()

# Global shit
ADJACENT_POSITIONS = [(1,0), (-1,0), (0,1), (0,-1)]
seen = {}
part_two = False

def print_maze(maze):
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if maze[y][x] == "#":
                print("█", end="")
            elif maze[y][x] == ".":
                print(" ", end="")
            elif maze[y][x] == "@":
                print("●", end="")
            else:
                print(maze[y][x], end="")
        print("")


def get_start_pos(maze):
    start_pos = []
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if maze[y][x] == "@":
                start_pos.append((y,x))
    if not part_two:
        return start_pos[0]
    else:
        return tuple(start_pos)


def get_adjacent(pos):
    return [(pos[0]+adj[0], pos[1]+adj[1]) for adj in ADJACENT_POSITIONS]


def make_p2_maze(maze, pos):
    new_maze = maze[:]
    y, x = pos
    lm = list(maze[y-1])
    new_maze[y-1] = lm[:x-1] + ["@", "#", "@"] + lm[x+2:]
    lm = list(maze[y])
    new_maze[y] = lm[:x-1] + ["#", "#", "#"] + lm[x+2:]
    lm = list(maze[y+1])
    new_maze[y+1] = lm[:x-1] + ["@", "#", "@"] + lm[x+2:]

    return new_maze


def get_keys(maze, reached_keys, start_pos):
    keys = {}
    q = deque()
    q.append(start_pos)
    distances = {start_pos: 0}

    while q:
        pos = q.popleft()
        adj_pos = get_adjacent(pos)

        for p in adj_pos:
            tile = maze[p[0]][p[1]]

            if tile == "#":
                continue
            if p in distances:
                continue
            distances[p] = distances[pos] + 1
            if tile.isupper() and tile.lower() not in reached_keys: # door but no key
                continue
            if tile.islower() and tile not in reached_keys: # new key
                keys[tile] = (p, distances[p])
            else:
                q.append(p)
    return keys


def get_keys_p2(maze, reached_keys, start_pos):
    keys = {}
    for robot in range(len(start_pos)):
        curr_keys = get_keys(maze, reached_keys, start_pos[robot])
        for key in curr_keys:
            keys[key] = (curr_keys[key][0], curr_keys[key][1], robot)
    return keys


def move(maze, reached_keys, start_pos):
    rkeys = ''.join(sorted(reached_keys))

    if (start_pos, rkeys) in seen:
        return seen[(start_pos, rkeys)]

    if not part_two:
        keys = get_keys(maze, reached_keys, start_pos)
    else:
        keys = get_keys_p2(maze, reached_keys, start_pos)

    if not keys: # we good
        d = 0
    else:
        dists = []
        if not part_two:
            for tile in keys:
                pos, distance = keys[tile]
                dists.append(distance + move(maze, reached_keys + tile, pos))
        else:
            for tile in keys:
                (pos, distance, robot) = keys[tile]
                new_start_pos = []
                for i in range(len(start_pos)):
                    if i == robot:
                        new_start_pos.append(pos)
                    else:
                        new_start_pos.append(start_pos[i])
                dists.append(distance + move(maze, reached_keys + tile, tuple(new_start_pos)))

        d = min(dists)
    seen[(start_pos, rkeys)] = d
    return d


def solve_part_one():
    maze = data
    start_pos = get_start_pos(maze)
    reached_keys = ""

    return move(maze, reached_keys, start_pos)


def solve_part_two():
    global part_two
    global seen

    seen = {}
    pos = get_start_pos(data) # just to make the maze
    maze = make_p2_maze(data, pos)
    reached_keys = ""
    part_two = True
    start_pos = get_start_pos(maze)

    return move(maze, reached_keys, start_pos)


if __name__ == '__main__':
    print("p1:",solve_part_one())
    print("p2:",solve_part_two())
