f = open("../input/01", "r")
one_per_line = [int(line.rstrip('\n')) for line in f]
f.close()

def solve_part_one():
    for a in one_per_line:
        for b in one_per_line:
            if a != b  and a + b == 2020:
                return a*b

def solve_part_two():
    for a in one_per_line:
        for b in one_per_line:
            for c in one_per_line:
                if a != b and b != c and a != c and a + b + c == 2020:
                    return a*b*c

print("p1:", solve_part_one())
print("p2:", solve_part_two())
