import math

def get_data():
    data = [
            {"x":5, "y":4, "z":4, "vx":0, "vy":0, "vz":0},
            {"x":-11, "y":-11, "z":-3, "vx":0, "vy":0, "vz":0},
            {"x":0, "y":7, "z":0, "vx":0, "vy":0, "vz":0},
            {"x":-13, "y":2, "z":10, "vx":0, "vy":0, "vz":0}
            ]
    return data


def calc(moon_data):
    for moon in moon_data:
        for neighbour in moon_data:
            if moon != neighbour:
                if moon["x"] > neighbour["x"]:
                    moon["vx"] -= 1
                    neighbour["vx"] += 1
                if moon["y"] > neighbour["y"]:
                    moon["vy"] -= 1
                    neighbour["vy"] += 1
                if moon["z"] > neighbour["z"]:
                    moon["vz"] -= 1
                    neighbour["vz"] += 1
    apply_velocity(moon_data)


def apply_velocity(moon_data):
    for moon in moon_data:
        moon["x"] += moon["vx"]
        moon["y"] += moon["vy"]
        moon["z"] += moon["vz"]


def calc_energy(moon_data):
    total_energy = 0
    for moon in moon_data:
        pot = abs(moon["x"]) + abs(moon["y"]) + abs(moon["z"])
        kin = abs(moon["vx"]) + abs(moon["vy"]) + abs(moon["vz"])
        total_energy += pot*kin
    return total_energy


def lcm(x, y):
    return x*y//math.gcd(x, y)


def solve_part_one():
    moon_data_one = get_data()
    for _ in range(1000):
        calc(moon_data_one)
    print("p1:", calc_energy(moon_data_one))


def solve_part_two():
    moon_data_two = get_data()
    seen = set()
    repeat = {"x":0, "y":0, "z":0}
    curr = 0
    while True:
        calc(moon_data_two)

        if repeat["x"] and repeat["y"] and repeat["z"]:
            break
        # x y z are independent
        if not repeat["x"]:
            xpair = ""
            for moon in moon_data_two:
                xpair += str(moon["x"]) +","+  str(moon["vx"])
            if xpair in seen:
                repeat["x"] = curr
            else:
                seen.add(xpair)

        if not repeat["y"]:
            ypair = ""
            for moon in moon_data_two:
                ypair += str(moon["y"]) +","+  str(moon["vy"])
            if ypair in seen:
                repeat["y"] = curr
            else:
                seen.add(ypair)

        if not repeat["z"]:
            zpair = ""
            for moon in moon_data_two:
                zpair += str(moon["z"]) +","+  str(moon["vz"])
            if zpair in seen:
                repeat["z"] = curr
            else:
                seen.add(zpair)

        curr+=1
    print("p2:",lcm(lcm(repeat["x"], repeat["y"]), repeat["z"]))


if __name__ == '__main__':
    solve_part_one()
    solve_part_two()
