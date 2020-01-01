f = open("../input/1", "r")
data = [int(line.rstrip('\n')) for line in f]
f.close()

def do_2():
    seen = set()
    res = 0
    seen.add(res)
    seen_twice = None
    while True:
        for n in data:
            res += n
            if res in seen:
                return res
            seen.add(res)

print("p1:", sum(data))
print("p2:", do_2())
