with open('../input/04', 'r') as f:
    lines = f.readlines()

BOARD_SIZE = 5

bingo_numbers = [int(n) for n in lines[0].split(",")]

all_rows = [[int(num) for num in row.split()] for row in [line.rstrip() for line in lines[1:] if line != '\n']]
bingo_board_rows = [[all_rows[i + j * BOARD_SIZE] for i in range(BOARD_SIZE)] for j in range(len(all_rows) // BOARD_SIZE)]


def won(board, numbers_called):
    return any(all(number in numbers_called for number in row_col) for row_col in [*board, *zip(*board)])


def solve_part_one():
    numbers_called = []
    for n in bingo_numbers:
        numbers_called.append(n)
        for board in bingo_board_rows:
            if won(board, numbers_called):
                sum_uncalled = sum(n for line in board for n in line if n not in numbers_called)
                return sum_uncalled * n


def solve_part_two():
    numbers_called = []
    non_winners = bingo_board_rows[::]
    for n in bingo_numbers:
        numbers_called.append(n)
        for board in non_winners:
            if won(board, numbers_called):
                if len(non_winners) == 1:
                    sum_uncalled = sum(n for line in board for n in line if n not in numbers_called)
                    return sum_uncalled * n
                non_winners.remove(board)



if __name__ == '__main__':
    print("p1:", solve_part_one())
    print("p2:", solve_part_two())

