f = open("../input/10", "r")
one_per_line = sorted([int(line.rstrip('\n')) for line in f])
one_per_line = [0] + one_per_line + [max(one_per_line) + 3]
f.close()


def solve_part_one():
    diff_one = 0
    diff_three = 0

    for i in range(len(one_per_line)-1):
        diff = one_per_line[i+1] - one_per_line[i]
        if diff == 1:
            diff_one += 1
        elif diff == 3:
            diff_three += 1

    return diff_one * diff_three


def solve_part_two():
    mem = {}
    def solve(i):
        ans = 0

        if i == len(one_per_line)-1:
            return 1
        if i in mem:
            return mem[i]

        for j in range(i+1, len(one_per_line)):
            if one_per_line[j]-one_per_line[i] <= 3:
                ans += solve(j)

        mem[i] = ans
        return ans

    return solve(0)


if __name__ == '__main__':
    print("p1:", solve_part_one())
    print("p2:", solve_part_two())
