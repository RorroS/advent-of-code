from collections import defaultdict, Counter

with open('../input/06') as f:
    state = Counter([int(num)
                     for num in f.readline().strip().split(',')])


def solve(state, days):
    for _ in range(days):
        new_state = defaultdict(int)
        for key in state:
            if key == 0:
                new_state[6] += state[key]
                new_state[8] = state[key]
            else:
                new_state[key - 1] += state[key]
        state = new_state

    ans = 0
    for key in state:
        ans += state[key]
    return ans


if __name__ == '__main__':
    print('p1:', solve(state, 80))
    print('p2:', solve(state, 256))
