inp = open("../input/02").read().rstrip().split("\n")

def wrapping_paper_needed(measurements):
    a, b, c = (int(x) for x in measurements.split('x'))
    return 2 * (a * b + a * c + b * c) + min(a * b, a * c, b * c)


def ribbon_needed(measurements):
    nums = [int(x) for x in measurements.split('x')]
    smallest = min(nums)
    nums.remove(smallest)
    return 2 * smallest + 2 * min(nums) + (smallest * min(nums) * max(nums))


def solve_part_one():
    ans = 0
    for dim in inp:
        ans += wrapping_paper_needed(dim)
    return ans

def solve_part_two():
    ans = 0
    for dim in inp:
        ans += ribbon_needed(dim)
    return ans

if __name__ == '__main__':
    print("p1:", solve_part_one())
    print("p2:", solve_part_two())
