from collections import deque

def parse_input():
    raw_inp = open("../input/22").read().rstrip().split("\n\n")
    inp = [player.split(":\n")[1].split("\n") for player in raw_inp]
    decks = []
    for deck in inp:
        decks.append([int(x) for x in deck])

    return decks


def final_score(p):
    ans = 0
    for i in range(len(p)):
        ans += p.pop() * (i+1)
    return ans


def regular_combat(p1, p2):
    while p1 and p2:
        c1, c2 = p1.pop(0), p2.pop(0)
        if c1 > c2:
            p1 += [c1, c2]
        else:
            p2 += [c2, c1]

    return p1, p2


def recursive_combat(p1, p2):
    already_played = set()
    while p1 and p2:
        t1, t2 = tuple(p1), tuple(p2)
        if (t1, t2) in already_played:
            return p1, []
        already_played.add((t1, t2))

        c1, c2 = p1.pop(0), p2.pop(0)

        if c1 <= len(p1) and c2 <= len(p2):
            r1, r2 = recursive_combat(p1[:c1], p2[:c2])
            p1_won = len(r1) > 0
        else:
            p1_won = c1 > c2

        if p1_won:
            p1 += [c1, c2]
        else:
            p2 += [c2, c1]

    return p1, p2


def solve_part_one(p1, p2):
    p1, p2 = regular_combat(p1, p2)
    winner = p1 if p1 else p2
    return final_score(winner)


def solve_part_two(p1, p2):
    p1, p2 = recursive_combat(p1, p2)
    winner = p1 if p1 else p2
    return final_score(winner)


if __name__ == '__main__':
    p1, p2 = parse_input()
    print("p1:", solve_part_one(p1[:], p2[:]))
    print("p2:", solve_part_two(p1[:], p2[:]))


