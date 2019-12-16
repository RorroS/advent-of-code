f = open("../input/16", "r")
data = [int(num) for num in f.read().rstrip()]
f.close()

PATTERN = [0,1,0,-1]

def get_pat_elem(phase, index):
    pattern_len = 4 * phase
    return PATTERN[index % pattern_len // phase]

def solve_part_one(data):
    new_data = []
    for _ in range(100):
        for i in range(len(data)):
            sum_res = 0
            phase = i+1

            for j in range(i,len(data)):
                index = j+1
                dat_elem = data[j]
                pat_elem = get_pat_elem(phase, index)
                res = dat_elem * pat_elem
                sum_res += res

            new_data.append(abs(sum_res) % 10) # append unit only

        data = new_data
        new_data = []

    return int("".join(str(num) for num in data[:8]))


def solve_part_two(data):
    big_data = data * 10000
    offset = int("".join([str(num) for num in big_data[:7]]))
    # Offset the data because anything before the offset will
    # be multiplied by 0 and will not matter anyway.
    big_data = big_data[offset:]

    for _ in range(100):
        # This kinda assumes the offset is higher than len(big_data/2)
        # because that makes the pattern element 1 for the rest of the
        # digits. Not sure if it's like that for all unputs. Mine was.
        s = sum(big_data)
        new_data = []

        for i in range(len(big_data)):
            new_data.append(s%10) # append unit only
            s -= big_data[i]

        big_data = new_data

    return int("".join(str(num) for num in big_data[:8]))


if __name__ == '__main__':
    print("p1:", solve_part_one(data))
    print("p2:", solve_part_two(data))
