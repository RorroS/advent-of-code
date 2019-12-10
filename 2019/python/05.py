f = open("../input/5", "r")
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

def run_code(code, u_in):
    curr_index = 0
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
            code[val1] = u_in
            curr_index += 2
        elif opcode == OUT:
            val1 = code[curr_index+1]
            print(get_real_value(code, mode[0], val1))
            curr_index += 2
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
            break
        else:
            print("Something went wrong")

def solve_part_one():
    code = [i for i in intcode_program]
    run_code(code, 1)

def solve_part_two():
    code = [i for i in intcode_program]
    run_code(code, 5)

def get_real_value(code, mode, value):
    if mode == POSITION_MODE:
        return code[value]
    elif mode == IMMEDIATE_MODE:
        return value


if __name__ == '__main__':
    solve_part_one()
    solve_part_two()
