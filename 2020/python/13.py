import math

f = open("../input/13", "r")
et = int(f.readline().rstrip())
buses = [bus for bus in f.readline().rstrip().split(",")]
f.close()


def intable(bus):
    try:
        return int(bus)
    except ValueError:
        return False


def solve_part_one():
    departed = False
    curr_t = et
    while not departed:
        for bus in buses:
            if not intable(bus):
                continue

            bus = int(bus)
            if not curr_t % bus:
                return bus * (curr_t - et)
        curr_t += 1


def solve_part_two():
    bees = [(offset, int(bus)) for offset, bus in enumerate(buses) if intable(bus)]

    time, bus = bees[0]
    for offset, b in bees[1:]:
        while True:
            time += bus
            if not (time + offset) % b:
                break

        bus = math.lcm(bus, b)

    return time


if __name__ == '__main__':
    print("p1:", solve_part_one())
    print("p2:", solve_part_two())
