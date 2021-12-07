import copy

f = open("../input/03", "r")
one_per_line = [line.rstrip('\n') for line in f]
f.close()


def solve_part_one():
    bits = {}
    gamma_rate = ""
    epsilon_rate = ""

    for report in one_per_line:
        for i in range(len(report)):
            if i not in bits:
                bits[i] = [0, 0]

            if (report[i] == "0"):
                bits[i][0] += 1
            else:
                bits[i][1] += 1


    for bit in bits:
        if bits[bit][0] > bits[bit][1]:
            gamma_rate += "0"
            epsilon_rate += "1"
        else:
            gamma_rate += "1"
            epsilon_rate += "0"

    return int(gamma_rate, 2) * int(epsilon_rate, 2)


def solve_part_two():
    oxygen_generator_rating = one_per_line.copy()
    co2_scrubber_rating = one_per_line.copy()
    zeros = []
    ones = []

    for i in range(len(one_per_line[0])):
        if (len(oxygen_generator_rating) < 2):
            break

        for report in oxygen_generator_rating:
            if report[i] == "0":
                zeros.append(report)
            else:
                ones.append(report)

        if len(ones) >= len(zeros):
            oxygen_generator_rating = ones.copy()
        else:
            oxygen_generator_rating = zeros.copy()
        zeros.clear()
        ones.clear()

    for i in range(len(one_per_line[0])):
        if (len(co2_scrubber_rating) < 2):
            break

        for report in co2_scrubber_rating:
            if report[i] == "0":
                zeros.append(report)
            else:
                ones.append(report)

        if len(zeros) <= len(ones):
            co2_scrubber_rating = zeros.copy()
        else:
            co2_scrubber_rating = ones.copy()
        zeros.clear()
        ones.clear()

    return int(oxygen_generator_rating[0], 2) * int(co2_scrubber_rating[0], 2)


if __name__ == '__main__':
    print("p1:", solve_part_one())
    print("p2:", solve_part_two())

