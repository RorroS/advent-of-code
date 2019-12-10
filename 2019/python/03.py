f = open("../input/3", "r")
wires = [line.rstrip('\n') for line in f]
f.close()

w1 = wires[0].split(',')
w2 = wires[1].split(',')

w1_path = {}
w2_path = {}

x = 0
y = 0
steps = 0
for m in w1:
    dist = int(m[1:])
    for i in range(dist):
        if m[0] == 'U':
            y += 1
        elif m[0] == 'D':
            y -= 1
        elif m[0] == 'L':
            x -= 1
        elif m[0] == 'R':
            x += 1
        if (x,y) not in w1_path:
            w1_path[(x, y)] = steps
        steps += 1

x = 0
y = 0
steps = 0
for m in w2:
    dist = int(m[1:])
    for i in range(dist):
        if m[0] == 'U':
            y += 1
        elif m[0] == 'D':
            y -= 1
        elif m[0] == 'L':
            x -= 1
        elif m[0] == 'R':
            x += 1
        if (x,y) not in w2_path:
            w2_path[(x, y)] = steps
        steps += 1


closest_dist = float('inf')
least_step = float('inf')
for p in w1_path:
    if p in w2_path and p != (0,0):
        d = abs(0 - p[0]) + abs(0 - p[1])
        if d < closest_dist:
            closest_dist = d
        if least_step > w1_path[p] + w2_path[p]:
            least_step = w1_path[p] + w2_path[p]

print(closest_dist, least_step)
