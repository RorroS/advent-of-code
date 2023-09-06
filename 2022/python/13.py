from ast import literal_eval
from functools import cmp_to_key

testing = False
with open('../input/13_example' if testing else '../input/13') as f:
    packet_pairs = f.read().rstrip().split('\n\n')

    pairs = []
    for pair in packet_pairs:
        left, right = pair.split('\n')
        pairs.append([literal_eval(left), literal_eval(right)])


def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        return left - right
    if isinstance(left, int):
        left = [left]
    if isinstance(right, int):
        right = [right]

    for i in range(min(len(left), len(right))):
        result = compare(left[i], right[i])
        if result != 0:
            return result

    return len(left) - len(right)


def is_in_order(result):
    return result < 0


def solve_part_one():
    res = 0
    for i in range(len(pairs)):
        left, right = pairs[i]
        result = compare(left, right)
        if is_in_order(result):
            res += i + 1

    return res


def solve_part_two():
    div1, div2 = [[[2]], [[6]]]
    all_packets = [div1, div2]
    for pair in packet_pairs:
        left, right = pair.split('\n')
        all_packets += [literal_eval(left), literal_eval(right)]

    sorted_packets = sorted(all_packets, key=cmp_to_key(compare))
    return (sorted_packets.index(div1) + 1) * (sorted_packets.index(div2) + 1)


if __name__ == '__main__':
    print('p1:', solve_part_one())
    print('p2:', solve_part_two())
