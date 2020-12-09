import itertools

f = open("../input/09", "r")
one_per_line = [int(line.rstrip('\n')) for line in f]
f.close()


def solve_part_one():
    for i in range(len(one_per_line)-25):
        current_25 = one_per_line[i:i+25]
        combination_sums = [sum(c) for c in itertools.combinations(current_25, 2)]

        if not one_per_line[i+25] in combination_sums:
            return one_per_line[i+25]


def solve_part_two(p1):
    for i in range(2, len(one_per_line)):
        combinations = [one_per_line[j:j+i] for j in range(len(one_per_line))]
        combination_sums = [sum(c) for c in combinations]
        if p1 in combination_sums:
            seq = combinations[[sum(c) for c in combinations].index(p1)]
            ans = min(seq) + max(seq)
            return ans


if __name__ == '__main__':
    p1 = solve_part_one()
    print("p1:", p1)
    print("p2:", solve_part_two(p1))
