f = open("../input/1", "r")
data = [p for p in f.read().rstrip()]
f.close()

print(data.count("(") - data.count(")"))

floor = 0
for f in range(len(data)):
    if data[f] == "(":
        floor+=1
    elif data[f] == ")":
        floor-=1
    if floor == -1:
        print(f+1)
        break

