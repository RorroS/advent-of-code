testing = False
with open('../input/01_example' if testing else '../input/01') as f:
    pairs = f.read().rstrip().split('\n')
    left = sorted([int(pair.split(' ')[0]) for pair in pairs])
    right = sorted([int(pair.split(' ')[-1]) for pair in pairs])

p1_res = 0
for i in range(len(left)):
    p1_res += abs(left[i] - right[i])
print("p1:", p1_res)

p2_res = 0
for n in left:
    p2_res += right.count(n) * n

print("p2:", p2_res)
