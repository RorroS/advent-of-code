import math

f = open("../input/14", "r")
data = [line.rstrip('\n') for line in f]
f.close()

def parse_data(data):
    prod_ing = {}
    for recipe in data:
        product = recipe.split(" => ")[1]
        product_name = product.split(" ")[1]
        product_amnt = int(product.split(" ")[0])

        ingredients = recipe.split(" => ")[0].split(", ")
        ings = []
        for ing in ingredients:
            ing_name = ing.split(" ")[1]
            ing_amnt = int(ing.split(" ")[0])
            ings.append((ing_amnt, ing_name))
        prod_ing[product_name] = (ings, (product_amnt, product_name))
    return prod_ing


def get_required_coal(products, fuel_amount):
    required = {}
    required['FUEL'] = fuel_amount

    while any(required[product] > 0 and product != "ORE" for product in required):
        product = ""

        for p in required:
            if required[p] > 0 and p != "ORE":
                product = p

        amnt_per_batch = products[product][1][0]

        times = math.ceil(required[product]/amnt_per_batch)

        required[product] -= amnt_per_batch*times

        for ingredient in products[product][0]:
            if ingredient[1] in required:
                required[ingredient[1]] += ingredient[0] * times
            else:
                required[ingredient[1]] = ingredient[0] * times

    return required['ORE']


def solve_part_one():
    products = parse_data(data)
    print("p1:", get_required_coal(products, 1))


def solve_part_two():
    products = parse_data(data)

    low=0
    high=int(1e12)
    while low<high:
        mid=(low+high+1)//2
        if get_required_coal(products, mid)<=int(1e12):
            low=mid
        else:
            high=mid-1

    print("p2:", low)


if __name__ == '__main__':
    solve_part_one()
    solve_part_two()
