from collections import deque

f = open("../input/20", "r")
data = [line.rstrip('\n') for line in f]
f.close()

WALKABLE = "."
ADJACENT_POSITIONS = [(1,0), (-1,0), (0,1), (0,-1)]

def get_adjacent(pos):
    return [(pos[0]+adj[0], pos[1]+adj[1]) for adj in ADJACENT_POSITIONS]


def get_adjacent_two(pos, grid):
    y, x = pos

    left_adj = grid[y][x-2:x]
    right_adj = grid[y][x+1:x+3]
    top_adj = grid[y-2][x]+grid[y-1][x]
    bottom_adj = grid[y+1][x]+grid[y+2][x]

    return [left_adj, right_adj, top_adj, bottom_adj]


def is_inner_portal(pos):
    return pos[0] >= 36 and pos[0] <= 92 and pos[1] >= 36 and pos[1] <= 98


def is_outer_portal(pos):
    return (pos[0] <= 2 and pos[1] >= 2 and pos[1] <= 132) or \
            (pos[0] >= 126 and pos[1] >= 2 and pos[1] <= 132) or \
            (pos[1] <= 2 and pos[0] >= 2 and pos[0] <= 126) or \
            (pos[1] >= 132 and pos[0] >= 2 and pos[0] <= 127)


def match_portals(grid):
    name_pos_pair = {}
    pos_pos_pair = {}

    for y in range(2, len(grid)-2): # skip outer space
        for x in range(2, len(grid[y])-2): # skip outer space
            if grid[y][x] != WALKABLE:
                continue
            pos = (y, x)
            adjacent = get_adjacent_two(pos, grid)
            for adj in adjacent:
                if adj.isalpha(): # AA BB etc
                    if adj in name_pos_pair:
                        pos_pos_pair[pos] = name_pos_pair[adj] #pos:pos
                        name_pos_pair[pos] = adj # pos:name
                        pos_pos_pair[name_pos_pair[adj]] = pos #flipped pos:pos
                    else:
                        name_pos_pair[adj] = pos #name:pos
                        name_pos_pair[pos] = adj #pos:name
    return name_pos_pair, pos_pos_pair


def solve(grid, part = 1):
    q = deque()
    start = "AA"
    end = "ZZ"
    seen = {}

    name_pos, pos_pos = match_portals(grid)
    # init q with start
    if part == 1:
        # (posistion, distance)
        q.append((name_pos[start], 0))
    else:
        # (posistion, distance, layer)
        q.append((name_pos[start], 0, 0))

    while q:
        if part == 1:
            pos, distance = q.popleft()

            if pos in seen:
                continue
            seen[pos] = distance
            if pos == name_pos[end]: # found goal
                return distance
            for p in get_adjacent(pos):
                if grid[p[0]][p[1]] == WALKABLE:
                    q.append((p, distance + 1))
            if pos in pos_pos: #teleport
                q.append((pos_pos[pos], distance + 1))
        else:
            pos, distance, layer = q.popleft()

            if (pos, layer) in seen:
                continue
            seen[(pos, layer)] = distance
            if pos == name_pos[end] and layer == 0: # found goal
                return distance
            for p in get_adjacent(pos):
                if grid[p[0]][p[1]] == WALKABLE:
                    q.append((p, distance + 1, layer))
            if pos in pos_pos: #teleport
                if is_inner_portal(pos): # teleport out and down
                    q.append((pos_pos[pos], distance + 1, layer + 1))
                elif is_outer_portal(pos) and layer > 0: # teleport in and up
                    q.append((pos_pos[pos], distance + 1, layer - 1))


def solve_part_one():
    print("p1:",solve(data))


def solve_part_two():
    print("p2:", solve(data, 2))


if __name__ == '__main__':
    solve_part_one()
    solve_part_two()
