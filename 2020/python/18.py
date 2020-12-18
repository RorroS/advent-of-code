import collections
import copy

with open("../input/18", "r") as f:
    lines = [line.rstrip().replace(" ", "") for line in f]
    inp = [collections.deque(line) for line in lines]


def eval_expr(expr, part_two):
    val = int(eval_left(expr, part_two))

    while expr and expr[0] != ")":
        ch = expr.popleft()

        if ch == "+":
            val += eval_left(expr, part_two)
        elif ch == "*":
            if part_two:
                val *= eval_expr(expr, part_two)
            else:
                val *= eval_left(expr, part_two)

    return val


def eval_left(expr, part_two):
    ch = expr.popleft()

    try:
        return int(ch)
    except ValueError:
        if ch == "(":
            val = eval_expr(expr, part_two)
            expr.popleft() # remove the last ). PAIN.
            return val


def solve_part_one():
    expressions = copy.deepcopy(inp)
    ans = 0
    for expression in expressions:
        ans += eval_expr(expression, False)

    return ans


def solve_part_two():
    expressions = copy.deepcopy(inp)
    ans = 0
    for expression in expressions:
        ans += eval_expr(expression, True)

    return ans


if __name__ == '__main__':
    print("p1:", solve_part_one())
    print("p2:", solve_part_two())
