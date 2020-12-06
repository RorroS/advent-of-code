f = open("../input/06", "r")
one_per_line = [line.rstrip('\n') for line in f]
f.close()

def build_groups():
    groups = []
    group = []
    for i in range(len(one_per_line)):
        if i == len(one_per_line)-1:
            group += [one_per_line[i]]
            groups.append(group)
            group = []
        elif one_per_line[i]:
            group += [one_per_line[i]]
        elif one_per_line[i] == '':
            groups.append(group)
            group = []
    return groups


def solve():
    groups = build_groups()

    sum_qs_p1 = 0
    sum_qs_p2 = 0
    for group in groups:
        answered_qs = []
        for member in group:
            for question in member:
                answered_qs.append(question)

        set_aqs = set(answered_qs)
        sum_qs_p1 += len(set_aqs)

        for q in set_aqs:
            if answered_qs.count(q) == len(group):
                sum_qs_p2 += 1

    return sum_qs_p1, sum_qs_p2


if __name__ == '__main__':
    p1, p2 = solve()
    print("p1:", p1)
    print("p2:", p2)
