import itertools


def map_and_count(inp):
    mapping = {}
    counts = {}

    for line in inp:
        ingredients, allergens = line.split(" (contains ")
        split_ingredients = ingredients.split()
        split_allergens = allergens.split(", ")

        for ingredient in split_ingredients:
            if ingredient not in counts:
                counts[ingredient] = 1
            else:
                counts[ingredient] += 1

        for allergen in split_allergens:
            if allergen not in mapping:
                mapping[allergen] = set(split_ingredients)
            else:
                mapping[allergen] = mapping[allergen].intersection(set(split_ingredients))

    return mapping, counts


def solve_part_one(mapping, counts):
    for allergen in mapping:
        for p in mapping[allergen]:
            if p in counts:
                del counts[p]
    ans = 0
    for c in counts:
        ans += counts[c]
    return ans


def solve_part_two(mapping):
    combs = list(itertools.permutations([k for k in mapping], 2))
    while False in [len(val) == 1 for val in mapping.values()]:
        for a, b in combs:
            if len(mapping[a]) == 1:
                mapping[b] = mapping[b].difference(mapping[a])

    return ','.join([mapping[x].pop() for x in sorted([k for k in mapping])])


if __name__ == '__main__':
    inp = [line.rstrip(")\n") for line in open("../input/21").readlines()]
    mapping, counts = map_and_count(inp)
    print("p1:", solve_part_one(mapping, counts))
    print("p2:", solve_part_two(mapping))
