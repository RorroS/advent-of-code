from copy import copy
f = open("../input/6", "r")
orbits = [line.rstrip('\n') for line in f]
f.close()

def make_dict(data):
    res = {}
    for orbit in data:
        parent, child = orbit.split(")")
        res[child] = parent
    return res

def get_all_orbits(data):
    res = 0
    for child in data:
        while child in data:
            parent = data[child]
            res += 1
            child = parent
    return res

def get_path_length(data, source, dest):
    paths = {source: [], dest: []}
    
    current = source
    while current in data:
        parent = data[current]
        paths[source].append(parent)
        current = parent

    current = dest
    while current in data:
        parent = data[current]
        paths[dest].append(parent)
        current = parent


    final_paths = paths.copy()

    while final_paths[source][-1] == final_paths[dest][-1]:
        final_paths[source].pop()
        final_paths[dest].pop()

    return len(final_paths[source]+final_paths[dest])


def solve_part_one(data):
    dic = make_dict(data)
    print("p1:",get_all_orbits(dic))

def solve_part_two(data, source, dest):
    dic = make_dict(data)
    print("p2:",get_path_length(dic, source, dest))

if __name__ == '__main__':
    solve_part_one(orbits)
    solve_part_two(orbits, "YOU", "SAN")
