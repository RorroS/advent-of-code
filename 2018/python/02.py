f = open("../input/2", "r")
data = [line.rstrip('\n') for line in f]
f.close()

twos = 0
threes = 0

for st in data:
    count = {}
    for c in st:
        if c not in count:
            count[c] = 1
        else:
            count[c] += 1

    twos += any(count[i] == 2 for i in count)
    threes += any(count[i] == 3 for i in count)

s1 = None
s2 = None
for st1 in data:
    for st2 in data:
        diff = 0
        for i in range(len(st1)):
            if st1[i] != st2[i]:
                diff += 1
        if diff == 1:
            s1 = st1
            s2 = st2
            break

res = ""
for i in range(len(s1)):
    if s1[i] == s2[i]:
        res += s1[i]

print("p1:", twos * threes)
print("p2:", res)

