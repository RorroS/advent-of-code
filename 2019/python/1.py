f = open("../input/1", "r")
modules = [int(line.rstrip('\n')) for line in f]
f.close()

p1_total = 0
p2_total = 0

for mod in modules:
    current = mod
    p1_total += (mod // 3) - 2

    while current > 0:
        current = (current // 3) - 2

        if current > 0:
            p2_total += current

print("p1:", p1_total, "\np2:", p2_total)
