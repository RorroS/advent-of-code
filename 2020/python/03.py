f = open("../input/03", "r")
one_per_line = [line.rstrip('\n') for line in f]
f.close()

def tree_count(step_x, step_y):
    map_length = len(one_per_line)
    map_width = len(one_per_line[0])
    curr_x = 0
    trees = 0

    for curr_y in range(0, map_length, step_y):
        if one_per_line[curr_y][(curr_x) % map_width] == '#':
            trees += 1
        curr_x += step_x

    return trees


if __name__ == '__main__':
    print("p1:", tree_count(3, 1))
    print("p2:", tree_count(1, 1) * \
                 tree_count(3, 1) * \
                 tree_count(5, 1) * \
                 tree_count(7, 1) * \
                 tree_count(1, 2))
