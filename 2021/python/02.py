f = open("../input/02", "r")
one_per_line = [line.rstrip('\n') for line in f]
f.close()


def solve_part_one():
    depth = 0
    h_pos = 0

    for instruction in one_per_line:
        command, amt = instruction.split(' ')
        if command == "forward":
            h_pos += int(amt)
        elif command == "up":
            depth -= int(amt)
        else:
            depth += int(amt)

    return depth * h_pos


def solve_part_two():
    depth = 0
    h_pos = 0
    aim = 0

    for instruction in one_per_line:
        command, amt = instruction.split(' ')
        if command == "forward":
            h_pos += int(amt)
            depth += aim * int(amt)
        elif command == "up":
            aim -= int(amt)
        else:
            aim += int(amt)

    return depth * h_pos


if __name__ == '__main__':
    print("p1:", solve_part_one())
    print("p2:", solve_part_two())

