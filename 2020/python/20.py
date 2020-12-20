import numpy as np

with open("../input/20", "r") as f:
    split = f.read().rstrip().split("\n\n")

    tiles = {}
    for tile_data in split:
        split_tile = tile_data.split(":\n")
        tle_nr = split_tile[0].split(" ")[1]

        tle = split_tile[1].split("\n")
        tle_lst = []
        for row in tle:
            tle_lst.append(list(row))

        tiles[tle_nr] = np.array(tle_lst)


def find_corners():
    corners = {}
    for t1 in tiles:
        sides_matched = 0
        for t2 in tiles:
            temp_t1 = tiles[t1]
            if t1 != t2:
                for i in range(0, 4):
                    temp_t1 = np.rot90(temp_t1, i)
                    if all(temp_t1[0] == tiles[t2][0]) or \
                       all(temp_t1[0] == np.rot90(tiles[t2])[0]) or \
                       all(temp_t1[0] == np.rot90(tiles[t2], 2)[0]) or \
                       all(temp_t1[0] == np.rot90(tiles[t2], 3)[0]) or \
                       all(temp_t1[0][::-1] == tiles[t2][0]) or \
                       all(temp_t1[0][::-1] == np.rot90(tiles[t2])[0]) or \
                       all(temp_t1[0][::-1] == np.rot90(tiles[t2], 2)[0]) or \
                       all(temp_t1[0][::-1] == np.rot90(tiles[t2], 3)[0]):
                        sides_matched += 1

        if sides_matched == 2:
            corners[t1] = tiles[t1]
    return corners


def solve_part_one():
    corners = find_corners()
    ans = 1
    for c in corners:
        ans *= int(c)
    return ans


if __name__ == '__main__':
    print("p1:", solve_part_one())


#mhead = '''..#.
#.###
##...'''
#ts_in_m = 15
#
#def trim_tiles():
#    new_tiles = {}
#    for t in tiles:
#        new_tile = []
#        for i in range(1, len(tiles[t])-1):
#            new_tile.append(tiles[t][i][1:-1])
#
#        new_tiles[t] = new_tile
#    return new_tiles
#
#new_tiles = trim_tiles()
#def count_tiles():
#    total_hash = 0
#    for t in new_tiles:
#        for p in new_tiles[t]:
#            for i in p:
#                if i == "#":
#                    total_hash += 1
#    return total_hash
#
#
##25 is the magic number
#print(count_tiles() - (ts_in_m * 25))
