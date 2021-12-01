f = open("../input/01", "r")
one_per_line = [int(line.rstrip('\n')) for line in f]
f.close()

def solve_part_one():
    increased = 0
    for i in range(len(one_per_line)-1):
        increased += one_per_line[i+1] > one_per_line[i]

    return increased


def solve_part_two():
    increased = 0
    previous_measurement = 0
    for i in range(len(one_per_line)-3):
        measurement = sum(one_per_line[i:i+3])

        increased += measurement > previous_measurement
        previous_measurement = measurement

    return increased

if __name__ == '__main__':
    print("p1:", solve_part_one())
    print("p2:", solve_part_two())

