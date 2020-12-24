inp = open("../input/03").read().rstrip()

def solve_part_one():
    seen = set()
    x = y = 0
    seen.add((0, 0))
    for d in inp:
        if d == '>':
            x += 1
        elif d == '<':
            x -= 1
        elif d == '^':
            y += 1
        else:
            y -= 1

        if (x, y) not in seen:
            seen.add((x, y))

    return len(seen)


def solve_part_two():
    pass
    seen = set()
    seen.add((0, 0))
    pos = [[0, 0], [0, 0]]
    for i in range(len(inp)):
        d = inp[i]
        if d == '>':
            pos[i%2][0] += 1
        elif d == '<':
            pos[i%2][0] -= 1
        elif d == '^':
            pos[i%2][1] += 1
        else:
            pos[i%2][1] -= 1

        if (pos[i%2][0], pos[i%2][1]) not in seen:
            seen.add((pos[i%2][0], pos[i%2][1]))

    return len(seen)


if __name__ == '__main__':
    print("p1:", solve_part_one())
    print("p2:", solve_part_two())
