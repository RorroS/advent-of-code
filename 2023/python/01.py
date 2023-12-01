testing = False
with open('../input/01_example' if testing else '../input/01') as f:
    rows = [line.strip() for line in f.readlines()]


def solve_part_one(inp):
    calibration_values = []

    for row in inp:
        numbers = [num for num in row if num.isdigit()]
        if numbers:
            calibration_values.append(int(numbers[0]+numbers[-1]))
    return sum(calibration_values)


numbers = {'one': '1', 'two': '2', 'three': '3', 'four': '4',
           'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}


def replace(row):
    for num in numbers:
        row = row.replace(num, num + numbers[num] + num)

    return row


def solve_part_two():
    new_rows = []
    for row in rows:
        new_rows.append(replace(row))

    result = solve_part_one(new_rows)
    return result


if __name__ == '__main__':
    print('p1:', solve_part_one(rows))
    print('p2:', solve_part_two())
