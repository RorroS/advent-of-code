inp = [l.rstrip() for l in open("../input/05").readlines()]

def enough_vowels(word):
    cnt = 0
    for ch in 'aeiou':
        cnt += word.count(ch)
    return cnt >= 3


def double_letter(word):
    for i in range(len(word) - 1):
        if word[i] == word[i+1]:
            return True
    return False


def banned_words(word):
    banned = ['ab', 'cd', 'pq', 'xy']
    for w in banned:
        if w in word:
            return True
    return False


def no_overlap_twice(word):
    for i in range(len(word) - 1):
        if word[i] + word[i+1] in word[i+2:]:
            return True
    return False


def repeat_letter_inbetween(word):
    for i in range(len(word) - 2):
        if word[i] == word[i+2]:
            return True
    return False


def solve_part_one():
    nice_strings = 0
    for word in inp:
        if not banned_words(word) and double_letter(word) and enough_vowels(word):
            nice_strings += 1

    return nice_strings


def solve_part_two():
    nice_strings = 0
    for word in inp:
        if no_overlap_twice(word) and repeat_letter_inbetween(word):
            nice_strings += 1

    return nice_strings


if __name__ == '__main__':
    print("p1:", solve_part_one())
    print("p2:", solve_part_two())
