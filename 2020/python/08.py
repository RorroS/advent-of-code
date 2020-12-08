f = open("../input/08", "r")
one_per_line = [line.rstrip('\n') for line in f]
f.close()


def run_instructions(instructions):
    acc = 0
    already_ran = []
    curr_instruction = 0

    while curr_instruction not in already_ran:
        already_ran.append(curr_instruction)

        try:
            split = instructions[curr_instruction].split(" ")
            inst = split[0]
            arg = split[1]
        except IndexError:
            return True, acc

        if inst == "jmp":
            curr_instruction += int(arg)
        elif inst == "acc":
            acc += int(arg)
            curr_instruction += 1
        else:
            curr_instruction += 1

    return False, acc


def solve_part_two():
    temp = one_per_line[:]

    for i in range(len(one_per_line)):
        if "jmp" in one_per_line[i]:
            temp[i] = 'nop ' + one_per_line[i].split()[1]
            terminated, ans = run_instructions(temp)

            if terminated:
                return ans


        temp = one_per_line[:]


if __name__ == '__main__':
    print("p1:", run_instructions(one_per_line)[1])
    print("p2:", solve_part_two())
