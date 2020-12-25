DIVIDER = 20201227
C = 8458505
D = 16050997

def get_loop_size(key):
    val = 1
    size = 0
    while True:
        if val == key:
            return size
        val = (val * 7) % DIVIDER
        size += 1


def get_encryption_key(key, loop_size):
    return pow(key, loop_size, DIVIDER)


def solve_part_one():
    return get_encryption_key(D, get_loop_size(C))


def solve_part_two():
    return "Click the button."


if __name__ == '__main__':
    print("p1:", solve_part_one())
    print("p2:", solve_part_two())
