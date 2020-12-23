inp = '496138527'

def do_moves(cups, n):
    ll = {a:b for a, b in zip(cups, cups[1:] + [cups[0]])}
    curr = cups[-1]

    for _ in range(n):
        curr = ll[curr]

        picked_up = []
        temp_curr = curr

        for _ in range(3):
            temp_curr = ll[temp_curr]
            picked_up.append(temp_curr)

        ll[curr] = ll[temp_curr]

        dest = curr - 1
        while dest in picked_up or dest < 1:
            dest -= 1
            if dest < 1:
                dest = max(cups)

        ll[dest], ll[picked_up[-1]] = picked_up[0], ll[dest]
    return ll


def solve_part_one():
    cups = [int(c) for c in inp]
    ll = do_moves(cups, 100)

    n = 1
    ans = ''
    for _ in range(8):
        n = ll[n]
        ans += str(n)

    return ans


def solve_part_two():
    cups = [int(c) for c in inp] + [i for i in range(10, 1_000_001)]
    ll = do_moves(cups, 10_000_000)

    n = 1
    ans = 1
    for _ in range(2):
        n = ll[n]
        ans *= n

    return ans


if __name__ == '__main__':
    print("p1:", solve_part_one())
    print("p2:", solve_part_two())
