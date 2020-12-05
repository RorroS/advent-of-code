f = open("../input/05", "r")
one_per_line = [line.rstrip('\n') for line in f]
f.close()

def search(low, high, combination):
    l = low
    h = high
    for ch in combination:
        mid = l + (h - l) // 2
        if ch in "BR":
            l = mid+1
        else:
            h = mid
    return l


def solve():
    ids = []
    for c in one_per_line:
        row_comb = c[:-3]
        row = search(0, 127, row_comb)

        col_comb = c[-3:]
        col = search(0, 7, col_comb)

        seat_id = row * 8 + col

        ids.append(seat_id)

    sorted_ids = sorted(ids)
    temp_id = sorted_ids[0]
    last_id = sorted_ids[-1]

    while temp_id in sorted_ids:
        temp_id += 1

    return sorted_ids[-1], temp_id


if __name__ == '__main__':
    p1, p2 = solve()
    print("p1:", p1)
    print("p2:", p2)
