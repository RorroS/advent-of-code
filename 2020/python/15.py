with open('../input/15') as f:
    starting_numbers = [int(num) for num in f.readline().strip().split(',')]


def get_nth(nth):
    previous = starting_numbers[-1]
    spoken_numbers = {num: i+1 for i, num in enumerate(starting_numbers)}

    for i in range(len(starting_numbers) + 1, nth + 1):
        if previous in spoken_numbers:
            current = i - spoken_numbers[previous] - 1
        else:
            current = 0

        spoken_numbers[previous] = i - 1
        previous = current

    return previous


if __name__ == '__main__':
    print("p1:", get_nth(2020))
    print("p2:", get_nth(30000000))
