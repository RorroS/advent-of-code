from collections import Counter

with open('../input/10') as f:
    chunks = [line.strip() for line in f]


openings = {'(': ')', '[': ']', '{': '}', '<': '>'}
closings = {')': '(', ']': '[', '}': '{', '>': '<'}
corrupt_points = {')': 3, ']': 57, '}': 1197, '>': 25137}
incomplete_points = {')': 1, ']': 2, '}': 3, '>': 4}


def solve_part_one():
    ans = 0
    for line in chunks:
        stack = []
        for char in line:
            if char in openings:
                stack.append(char)
            # valid ending
            elif char in corrupt_points and len(stack) > 0 and stack[-1] == closings[char]:
                stack.pop()
            else:  # corrupt line
                ans += corrupt_points[char]
                break

    return ans


def solve_part_two():
    scores = []
    for line in chunks:
        stack = []
        corrupt = False
        for char in line:
            if char in openings:
                stack.append(char)
            # valid ending
            elif char in corrupt_points and len(stack) > 0 and stack[-1] == closings[char]:
                stack.pop()
            else:  # corrupt line
                corrupt = True
                break
        if corrupt:  # ignore corrupt lines
            continue

        score = 0
        for incomplete in stack[::-1]:
            score = 5 * score + incomplete_points[openings[incomplete]]
        scores.append(score)

    return sorted(scores)[len(scores)//2]


if __name__ == '__main__':
    print('p1:', solve_part_one())
    print('p2:', solve_part_two())
