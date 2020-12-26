inp = [line.rstrip() for line in open("../input/06").readlines()]

def solve_part_one():
    lights = [[False for _ in range(1000)] for _ in range(1000)]

    for instr in inp:
        split = instr.split()
        if split[0] == "toggle":
            x1, y1 = split[1].split(",")
            x2, y2 = split[3].split(",")
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

            for i in range(y1, y2+1):
                for j in range(x1, x2+1):
                    lights[i][j] = not lights[i][j]
        else:
            x1, y1 = split[2].split(",")
            x2, y2 = split[4].split(",")
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

            for i in range(y1, y2+1):
                for j in range(x1, x2+1):
                    lights[i][j] = True if split[1] == "on" else False

    ans = 0
    for i in range(1000):
        ans += sum(lights[i])
    return ans


def solve_part_two():
    lights = [[0 for _ in range(1000)] for _ in range(1000)]

    for instr in inp:
        split = instr.split()
        if split[0] == "toggle":
            x1, y1 = split[1].split(",")
            x2, y2 = split[3].split(",")
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

            for i in range(y1, y2+1):
                for j in range(x1, x2+1):
                    lights[i][j] += 2

        else:
            x1, y1 = split[2].split(",")
            x2, y2 = split[4].split(",")
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

            for i in range(y1, y2+1):
                for j in range(x1, x2+1):
                    if split[1] == "on":
                        lights[i][j] += 1
                    else:
                        if lights[i][j] > 0:
                            lights[i][j] -= 1

    ans = 0
    for i in range(1000):
        ans += sum(lights[i])
    return ans


if __name__ == '__main__':
    print("p1:", solve_part_one())
    print("p2:", solve_part_two())
