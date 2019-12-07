import itertools

f = open("../input/7", "r")
intcode_program = [int(num) for num in f.read().rstrip().split(',')]
f.close()

ADD = 1
MUL = 2
IN = 3
OUT = 4
JMP_IF_TRUE = 5
JMP_IF_FALSE = 6
LESS_THAN = 7
EQUALS = 8
TERMINATE = 99

POSITION_MODE = 0
IMMEDIATE_MODE = 1

def run_code(code_in, u_in, curr_index):     
    code = [x for x in code_in]
    while True:
        opcode = code[curr_index]%100
        mode = [(code[curr_index] // 100)%10, code[curr_index]//1000]

        if opcode == ADD:
            val1, val2, dest = code[curr_index+1], code[curr_index+2], code[curr_index+3] 
            code[dest] = get_real_value(code, mode[0], val1) + get_real_value(code, mode[1], val2)
            curr_index += 4
        elif opcode == MUL:
            val1, val2, dest = code[curr_index+1], code[curr_index+2], code[curr_index+3] 
            code[dest] = get_real_value(code, mode[0], val1) * get_real_value(code, mode[1], val2)
            curr_index += 4
        elif opcode == IN:
            val1 = code[curr_index+1]
            code[val1] = u_in[0]
            u_in.pop(0)
            curr_index += 2
        elif opcode == OUT:
            val1 = code[curr_index+1]
            curr_index += 2
            return get_real_value(code, mode[0], val1), curr_index
        elif opcode == JMP_IF_TRUE:
            val1, val2 = code[curr_index+1], code[curr_index+2]
            if get_real_value(code, mode[0], val1) != 0:
                curr_index = get_real_value(code, mode[1], val2)
            else:
                curr_index+=3
        elif opcode == JMP_IF_FALSE:
            val1, val2 = code[curr_index+1], code[curr_index+2]
            if get_real_value(code, mode[0], val1) == 0:
                curr_index = get_real_value(code, mode[1], val2)
            else:
                curr_index+=3
        elif opcode == LESS_THAN:
            val1, val2, dest = code[curr_index+1], code[curr_index+2], code[curr_index+3] 
            if get_real_value(code, mode[0], val1) < get_real_value(code, mode[1], val2):
                code[dest]=1
            else:
                code[dest]=0
            curr_index+=4
        elif opcode == EQUALS:
            val1, val2, dest = code[curr_index+1], code[curr_index+2], code[curr_index+3] 
            if get_real_value(code, mode[0], val1) == get_real_value(code, mode[1], val2):
                code[dest]=1
            else:
                code[dest]=0
            curr_index+=4
        elif opcode == TERMINATE:
            assert opcode == 99, opcode
            return None, curr_index
        else:
            print("Something went wrong")
        


def get_real_value(code, mode, value):
    if mode == POSITION_MODE:
        return code[value]
    elif mode == IMMEDIATE_MODE:
        return value


def get_permutations(num_set):
    permutations = []
    for subset in itertools.permutations(num_set, len(num_set)):
        permutations.append(subset)
    return permutations


def solve_part_one():
    copy = [i for i in intcode_program]
    permutations = get_permutations([0,1,2,3,4])
    res = 0

    for p in permutations:
        next_val = 0
        for i in p:
            next_val, _ = run_code(copy, [i, next_val], 0)
        if next_val > res:
            res = next_val
    return res


def solve_part_two():
    copy = [i for i in intcode_program]
    permutations = get_permutations([5,6,7,8,9])
    res = 0

    for p in permutations:
        next_val = 0
        
        # index for each run
        ind = [0, 0, 0, 0, 0]

        # last output for each run
        last_output = [0, 0, 0, 0, 0]

        # list of inputs for each run, first always start at 0
        in_lst = [[p[0], 0], [p[1]], [p[2]], [p[3]], [p[4]]]

        halt = False

        while not halt:
            for i in range(len(p)):
                next_val, curr_index = run_code(intcode_program, in_lst[i], ind[i])

                # if not terminated
                if next_val != None:
                    if next_val > res:
                        res = next_val
                else:
                    halt = True
                    break

                next_in = (i+1)%5
                in_lst[next_in].append(next_val)
                ind[i] = curr_index
    return res


if __name__ == '__main__':
    print("p1:", solve_part_one())
    print("p2:", solve_part_two())
