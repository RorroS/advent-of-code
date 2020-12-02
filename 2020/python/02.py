f = open("../input/02", "r")
one_per_line = [line.rstrip('\n') for line in f]
f.close()


def solve_part_one():
    valid_pws = 0
    for p in one_per_line:
        lower_limit = int(p.split("-")[0])
        upper_limit = int(p.split(":")[0].split(" ")[0].split("-")[1])
        ch = p.split(":")[0].split(" ")[1]
        pw = p.split(" ")[2]

        if pw.count(ch) >= lower_limit and pw.count(ch) <= upper_limit:
            valid_pws += 1

    return valid_pws


def solve_part_two():
    valid_pws = 0
    for p in one_per_line:
        lower_limit = int(p.split("-")[0])
        upper_limit = int(p.split(":")[0].split(" ")[0].split("-")[1])
        ch = p.split(":")[0].split(" ")[1]
        pw = p.split(" ")[2]

        a = pw[lower_limit-1] == ch
        b = pw[upper_limit-1] == ch

        if a != b:
            valid_pws += 1

    return valid_pws

if __name__ == '__main__':
    print("p1:", solve_part_one())
    print("p2:", solve_part_two())
