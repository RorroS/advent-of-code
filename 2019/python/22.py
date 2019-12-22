f = open("../input/22", "r")
data = [line.rstrip('\n') for line in f]
f.close()

def deal_new_stack(deck):
    return deck[::-1]

def cut(deck, n):
    return deck[n:] + deck[:n]

def deal_increment(deck, n):
    res = [None for _ in range(len(deck))]

    for i in range(len(deck)):
        pos = (i * n) % len(deck)
        res[pos] = deck[i]

    return res


def solve_part_one():
    shuffles = data[:]
    cards = list(range(10007))

    for shuffle in shuffles:
        lst_shuffle = shuffle.split(" ")

        if lst_shuffle[0] == "cut":
            n = int(lst_shuffle[1])
            cards = cut(cards, n)

        elif lst_shuffle[0] == "deal":
            if lst_shuffle[-1].isalpha():
                cards = deal_new_stack(cards)
            else:
                n = int(lst_shuffle[-1])
                cards = deal_increment(cards, n)

        else:
            return "Something ain't right dawg"

    return cards.index(2019)

def mmi(cards, n):
    return pow(n, cards-2, cards)

def get_nth(cards, offset, increment, n):
    return (offset + n * increment) % cards

def solve_part_two():
    shuffles = data[:]

    cards = 119315717514047
    repeats = 101741582076661

    cards_1 = 10007
    repeats_1 = 1

    #increment per index
    increment = 1
    # first number
    offset = 0

    for shuffle in shuffles:
        lst_shuffle = shuffle.split(" ")

        if lst_shuffle[0] == "cut": # cut 10
            n = int(lst_shuffle[1])
            offset += n * increment

        elif lst_shuffle[0] == "deal":
            if lst_shuffle[-1].isalpha(): # deal into new stack
                increment *= -1 # just go the other way
                offset += increment

            else: # deal with increment 10
                n = int(lst_shuffle[-1])
                increment *= mmi(cards, n) #modular multiplicative inverse

        else:
            return "Something ain't right dawg"

    i = pow(increment, repeats, cards)
    o = offset * (1 - i) * mmi(cards, (1 - increment))

    return get_nth(cards, o, i, 2020)


if __name__ == '__main__':
    print("p1:", solve_part_one())
    print("p2:", solve_part_two())
