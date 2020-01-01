f = open("../input/1", "r")
data = [int(p) for p in f.read().rstrip()]
f.close()

res = 0
for i in range(len(data)):
    if data[i] == data[(i+1) % len(data)]:
        res+=data[i]

print(res)

res = 0
for i in range(len(data)):
    if data[i] == data[(i+len(data)//2) % len(data)]:
        res+=data[i]

print(res)
