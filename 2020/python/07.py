f = open("../input/07", "r")
one_per_line = [line.rstrip('\n') for line in f]
f.close()

bags = {}
for p in one_per_line:
    split = p.split(" bags contain ")
    outer_bag = split[0]
    inner_bags = [bag[:bag.find(" bag")] for bag in split[1].split(", ")]

    if inner_bags[0] == "no other":
        bags[outer_bag] = dict()
    else:
        bags[outer_bag] = {bag[2:]: int(bag[0]) for bag in inner_bags}


def solve_part_one():
    ans = set()
    q = ["shiny gold"]
    reverse_bags = {}
    for outer_bag in bags:
        if bags[outer_bag]:
            for inner_bag in bags[outer_bag]:
                if inner_bag in reverse_bags:
                    reverse_bags[inner_bag].append(outer_bag)
                else:
                    reverse_bags[inner_bag] = [outer_bag]

    while q:
        try:
            ans.add(q[0])
            q += reverse_bags[q[0]]
        except KeyError:
            pass
        finally:
            del q[0]

    return len(ans) - 1


def solve_part_two():
    ans = 0
    q = [("shiny gold", 1)]

    while q:
        for bag in bags[q[0][0]]:
            ans += bags[q[0][0]][bag] * q[0][1]
            q.append((bag, bags[q[0][0]][bag] * q[0][1]))
        del q[0]

    return ans


if __name__ == '__main__':
    print("p1:", solve_part_one())
    print("p2:", solve_part_two())
