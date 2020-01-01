import sys
f = open("../input/1", "r")
data = [inst.strip() for inst in f.read().rstrip().split(',')]
f.close()

def p1():
    x, y = 0,0
    curr_dr = "n"
    for inst in data:
        dr = inst[0]
        dist = int(inst[1:])

        if dr == "L":
            if curr_dr == "n":
                curr_dr = "w"
                x-=dist
            elif curr_dr == "s":
                curr_dr = "e"
                x+=dist
            elif curr_dr == "w":
                curr_dr = "s"
                y+=dist
            elif curr_dr == "e":
                curr_dr = "n"
                y-=dist

        if dr == "R":
            if curr_dr == "n":
                curr_dr = "e"
                x+=dist
            elif curr_dr == "s":
                curr_dr = "w"
                x-=dist
            elif curr_dr == "w":
                curr_dr = "n"
                y-=dist
            elif curr_dr == "e":
                curr_dr = "s"
                y+=dist

    print(abs(x)+abs(y))


def p2():
    x, y = 0,0
    dirs = {"n": (0,-1), "s":(0,1), "e":(1,0), "w":(-1,0)}
    curr_dr = "n"
    seen = set()
    seen.add((x,y))
    for inst in data:
        dr = inst[0]
        dist = int(inst[1:])

        for i in range(1, dist+1):
            if dr == "L":
                if curr_dr == "n":
                    x-=1
                elif curr_dr == "s":
                    x+=1
                elif curr_dr == "w":
                    y+=1
                elif curr_dr == "e":
                    y-=1

            if dr == "R":
                if curr_dr == "n":
                    x+=1
                elif curr_dr == "s":
                    x-=1
                elif curr_dr == "w":
                    y-=1
                elif curr_dr == "e":
                    y+=1

            if (x,y) in seen:
                print(abs(x)+abs(y))
                sys.exit(0)
            else:
                seen.add((x,y))

        if dr == "L":
            if curr_dr == "n":
                curr_dr = "w"
            elif curr_dr == "s":
                curr_dr = "e"
            elif curr_dr == "w":
                curr_dr = "s"
            elif curr_dr == "e":
                curr_dr = "n"

        if dr == "R":
            if curr_dr == "n":
                curr_dr = "e"
            elif curr_dr == "s":
                curr_dr = "w"
            elif curr_dr == "w":
                curr_dr = "n"
            elif curr_dr == "e":
                curr_dr = "s"


p1()
p2()
