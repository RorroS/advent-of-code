with open('../input/08') as f:
    inputs = []
    outputs = []
    for line in f:
        split = line.rstrip().split(' | ')
        inputs += split[0].split(' ')
        outputs += split[1].split(' ')

# segments: digit
unique_digits = {2: 1, 4: 4, 3: 7, 7: 8}


def solve_part_one():
    ans = 0
    for o in outputs:
        if (len(o) in unique_digits):
            ans += 1

    return ans


def containsAll(a, b):
    return all(x in b for x in a)


def decode_digits(input):
    X = {}
    input = [''.join(digit) for digit in input]
    for digit in input:  # Find known digits
        digit_len = len(digit)
        if digit_len in unique_digits:  # 1, 4, 7, 8
            X[unique_digits[digit_len]] = digit

    for digit in input:
        if len(digit) == 6:  # 0, 6, 9
            if not containsAll(X[1], digit):  # 6
                X[6] = digit
            elif containsAll(X[4], digit):  # 9
                X[9] = digit
            else:  # 0
                X[0] = digit

    for digit in input:
        if len(digit) == 5:  # 2, 3, 5
            if containsAll(X[1], digit):  # 3
                X[3] = digit
            elif containsAll(digit, X[6]):  # 5
                X[5] = digit
            else:  # 2
                X[2] = digit

    return X


def solve_part_two():
    ans = 0

    new_input = [inputs[x:x+10] for x in range(0, len(inputs), 10)]
    new_output = [outputs[x:x+4] for x in range(0, len(outputs), 4)]

    for i in range(len(new_input)):
        decoded_output = ''
        decoded_input = decode_digits(new_input[i])
        for o in new_output[i]:
            for d in decoded_input:
                if len(o) == len(decoded_input[d]) and all(x in decoded_input[d] for x in o):
                    decoded_output += str(d)
        ans += int(decoded_output)

    return ans


if __name__ == '__main__':
    print('p1:', solve_part_one())
    print('p2:', solve_part_two())
