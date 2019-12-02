ADD = 1
MUL = 2
TERMINATE = 99

f = open("../input/2", "r")
intcode_program = [int(num) for num in f.read().rstrip().split(',')]
f.close()

def run_intcode(code):
    curr_index = 0
    opcode = code[curr_index]

    while opcode != TERMINATE:
        val1_index = code[curr_index + 1]
        val2_index = code[curr_index + 2]
        dest_index = code[curr_index + 3]

        if opcode == ADD:
            code[dest_index] = code[val1_index] + code[val2_index]
        elif opcode== MUL:
            code[dest_index] = code[val1_index] * code[val2_index]
        else:
            print("Something went wrong")

        curr_index += 4
        opcode = code[curr_index]
    return code

def solve_part_one():
    res = [num for num in intcode_program]
    res[1] = 12
    res[2] = 2

    print("p1:", run_intcode(res)[0])

def solve_part_two():
    for i in range(0, 100):
        for j in range(0, 100):
            res = [num for num in intcode_program]
            res[1] = i
            res[2] = j

            res = run_intcode(res)

            if res[0] == 19690720:
                print("p2:", 100 * res[1] + res[2])

if __name__ == '__main__':
    solve_part_one()
    solve_part_two()
