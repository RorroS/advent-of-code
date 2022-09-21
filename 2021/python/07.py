import sys

with open('../input/07') as f:
    positions = [int(x) for x in f.readline().rstrip().split(',')]
    positions.sort()


def solve_part_one():
    ans = 0
    median = positions[len(positions)//2]
    for p in positions:
        ans += abs(p-median)
    return ans


def solve_part_two():
    ans = sys.maxsize
    for i in range(2000):  # 2000 because it's larger than max in input
        current = 0
        for p in positions:
            delta = abs(p-i)
            current += delta*(delta+1)//2

        if current < ans:
            ans = current
    return ans


if __name__ == '__main__':
    print('p1:', solve_part_one())
    print('p2:', solve_part_two())
