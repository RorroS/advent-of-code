with open("../input/16", "r") as f:
    sections = [s.rstrip() for s in f.read().split("\n\n")]

    values = {}
    for val in sections[0].split("\n"):
        split = val.split(": ")
        n = split[0]
        r_split = split[1].split(" or ")
        r1 = tuple([int(i) for i in r_split[0].split("-")])
        r2 = tuple([int(i) for i in r_split[1].split("-")])
        values[n] = [r1, r2]

    my_ticket = [int(i) for i in sections[1].split("\n")[1].split(",")]

    nearby_tickets = []
    for line in sections[2].split("\n")[1:]:
        nearby_tickets.append(tuple([int(i) for i in line.split(",")]))


def is_valid_ticket(ticket):
    num_categories = []
    for num in ticket:
        l_num = [num, []]
        valid = False
        for val in values:
            for r in values[val]:
                if r[0] <= num and num <= r[1]:
                    valid = True
                    l_num[1].append(val)

        if not valid:
            return False, num

        num_categories.append(l_num)

    return True, num_categories


def comfirm(possibs):
    comfirmed = {}
    for p in possibs:
        if len(possibs[p]) == 1:
            comfirmed[p] = possibs[p][0]

    return comfirmed


def solve_part_one():
    errors = []

    for ticket in nearby_tickets:
        valid, num = is_valid_ticket(ticket)
        if not valid:
            errors.append(num)

    return sum(errors)


def solve_part_two():
    valid_tickets = {}

    for ticket in nearby_tickets:
        valid, num_categories = is_valid_ticket(ticket)
        if valid:
            valid_tickets[ticket] = num_categories

    valid_tickets_keys = list(valid_tickets.keys())
    possibs = {}
    for i in range(len(valid_tickets_keys[0])): # from 0 to length of a ticket. Index of category
        ctgries = []
        for ticket in valid_tickets_keys:
            indexed_ticket = valid_tickets[ticket][i]
            possible_categories = indexed_ticket[1]
            ctgries.append(possible_categories)

        try:
            intersected = set(ctgries[0]).intersection(*ctgries)
        except ValueError:
            intersected = set()

        possibs[i] = list(intersected)

    comfirmed = {}
    while True:
        new_comfed = comfirm(possibs)
        if new_comfed:
            comfirmed.update(new_comfed)
            for p in new_comfed:
                del possibs[p]
                ctgry = new_comfed[p]
                for g in possibs:
                    possibs[g] = list(filter(lambda x: x != ctgry, possibs[g]))
        else:
            ans = 1
            for p in comfirmed:
                if "departure" in comfirmed[p]:
                    ans *= my_ticket[p]

            return ans


if __name__ == '__main__':
    print("p1:", solve_part_one())
    print("p2:", solve_part_two())
