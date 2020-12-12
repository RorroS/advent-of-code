f = open("../input/12", "r")
one_per_line = [line.rstrip('\n') for line in f]
f.close()


def solve_part_one():
    direction = 1
    xy = 0
    for cmd in one_per_line:
        instruction = cmd[0]
        amnt = int(cmd[1:])

        if instruction == 'N':
            xy += amnt * 1j
        if instruction == 'S':
            xy -= amnt * 1j
        if instruction == 'E':
            xy += amnt
        if instruction == 'W':
            xy -= amnt
        if instruction == 'F':
            xy += direction * amnt
        if instruction == 'R':
            direction /= 1j ** (amnt//90)
        if instruction == 'L':
            direction *= 1j ** (amnt//90)

    return int(abs(xy.real) + abs(xy.imag))


def solve_part_two():
    xy = 0
    wpxy = 10 + 1j

    for cmd in one_per_line:
        instruction = cmd[0]
        amnt = int(cmd[1:])

        if instruction == 'N':
            wpxy += amnt * 1j
        if instruction == 'S':
            wpxy -= amnt * 1j
        if instruction == 'E':
            wpxy += amnt
        if instruction == 'W':
            wpxy -= amnt
        if instruction == 'F':
            xy += wpxy * amnt
        if instruction == 'R':
            wpxy /= 1j ** (amnt//90)
        if instruction == 'L':
            wpxy *= 1j ** (amnt//90)

    return int(abs(xy.real) + abs(xy.imag))


if __name__ == '__main__':
    print("p1:", solve_part_one())
    print("p2:", solve_part_two())
