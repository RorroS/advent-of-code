inp = open("../input/24", "r").read().rstrip().splitlines()

DIRECTIONS = ['e', 'w', 'ne', 'se', 'nw', 'sw']

def turned(instr):
    i = x = y = 0
    while i < len(instr):
        if instr[i] == "e":
            x += 1
        elif instr[i] == "w":
            x -= 1
        else:
            if instr[i:i+2] == "ne":
                x += 1
                y -= 1
            elif instr[i:i+2] == 'se':
                y += 1
            elif instr[i:i+2] == 'nw':
                y -= 1
            elif instr[i:i+2] == 'sw':
                x -= 1
                y += 1
            i += 1
        i += 1
    return (x,y)


def add_tuples(a, b):
    return a[0] + b[0], a[1] + b[1]


def get_neighbours(tile):
    return [add_tuples(tile, turned(d)) for d in DIRECTIONS]


def solve_part_one():
    all_flipped = set()

    for line in inp:
        flipped = turned(line)
        if flipped in all_flipped:
            all_flipped.remove(flipped)
        else:
            all_flipped.add(flipped)

    return all_flipped


def solve_part_two(all_flipped):
    for _ in range(100):
        all_flipped_with_neighbours = set()
        for tile in all_flipped:
            all_flipped_with_neighbours.add(tile)
            neighbours = get_neighbours(tile)
            all_flipped_with_neighbours.update(neighbours)

        temp_all_flipped = set()
        for tile in all_flipped_with_neighbours:
            black_neighbours = 0
            neighbours = get_neighbours(tile)
            for neighbour in neighbours:
                if neighbour in all_flipped:
                    black_neighbours += 1

            if tile not in all_flipped and black_neighbours == 2 or \
                    tile in all_flipped and black_neighbours in [1,2]:
                temp_all_flipped.add(tile)
            else:
                continue

        all_flipped = temp_all_flipped

    return len(all_flipped)


if __name__ == '__main__':
    p1_ans = solve_part_one()
    print("p1:", len(p1_ans))
    print("p2:", solve_part_two(p1_ans))
