f = open("../input/3", "r")
data = [line.rstrip('\n') for line in f]
f.close()

claims = {}
for line in data:
    split_l = line.split(' ')
    c_id = split_l[0][1:]
    pos = (int(split_l[2].split(',')[0]), int(split_l[2].split(',')[1][:-1]))
    size = (int(split_l[3].split('x')[0]), int(split_l[3].split('x')[1]))

    claims[c_id] = (pos, size)


