import itertools

with open('../input/14', 'r') as f:
    one_per_line = []

    first_line = f.readline().rstrip()
    current_batch = [first_line]
    for line in f:
        if line.startswith("mask = "):
            one_per_line.append(current_batch)
            current_batch = [line.rstrip()]
        else:
            current_batch.append(line.rstrip())
    one_per_line.append(current_batch)


def pad(mask_len, val):
    return (mask_len - len(val)) * '0' + val


def add_value(mask, val):
    mask_len = len(mask)
    result = ['0' for _ in range(mask_len)]
    val = pad(mask_len, val)

    for i in range(mask_len):
        if mask[i] == '1':
            result[i] = '1'
        elif mask[i] == '0':
            result[i] = '0'
        else:
            result[i] = val[i]

    return int(''.join(result), 2)


def get_all_addresses(mask, address):
    mask_len = len(mask)
    result = ['0' for _ in range(mask_len)]
    addr = pad(mask_len, address)

    for i in range(mask_len):
        if mask[i] == '0':
            result[i] = addr[i]
        elif mask[i] == '1':
            result[i] = '1'
        else:
            result[i] = 'X'

    x_count = result.count("X")
    combinations = list(itertools.product(*(range(2) for _ in range(x_count))))

    all_addresses = []
    for c in combinations:
        c = list(c)
        temp_res = result[:]
        for i in range(len(result)):
            if result[i] == "X":
                temp_res[i] = str(c.pop(0))

        all_addresses.append(int(''.join(temp_res), 2))


    return all_addresses


def get_data(thing):
    split = thing.split(" = ")
    address = int(split[0][4:-1])
    val = bin(int(split[1])).replace("0b", "")
    bin_address = bin(address).replace("0b", "")

    return address, val, bin_address


def solve_part_one():
    memory = {}
    for b in one_per_line:
        mask = b[0].split(" = ")[1]

        for thing in b[1:]:
            address, val, _ = get_data(thing)

            added_value = add_value(mask, val)
            memory[address] = added_value

    res = 0
    for ad in memory:
        res += memory[ad]

    return res


def solve_part_two():
    memory = {}
    for b in one_per_line:
        mask = b[0].split(" = ")[1]

        for thing in b[1:]:
            address, _, bin_address = get_data(thing)
            val = int(thing.split(" = ")[1])
            all_addresses = get_all_addresses(mask, bin_address)

            for addr in all_addresses:
                memory[addr] = val


    res = 0
    for ad in memory:
        res += memory[ad]

    return res


if __name__ == '__main__':
    print("p1:", solve_part_one())
    print("p2:", solve_part_two())
