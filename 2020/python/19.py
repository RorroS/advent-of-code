with open("../input/19", "r") as f:
    rules, messages = f.read().split("\n\n")

    messages = messages.rstrip().split("\n")
    formatted_rules = {}

    for rule in rules.split("\n"):
        rule_data = rule.rstrip().split(": ")
        i = rule_data[0]

        inner_seq = []
        for seq in rule_data[1].split(" | "):
            _seq = []
            for r in seq.split(" "):
                try:
                    _seq.append(int(r))
                except ValueError:
                    _seq.append(r.strip('"'))
            inner_seq.append(_seq)

        formatted_rules[int(i)] = inner_seq


def is_valid(i, message, start):
    rule = formatted_rules[i]
    if isinstance(rule[0][0], str):
        s = set()
        if start < len(message) and rule[0][0] == message[start]:
            s.add(start + 1)
        return s
    else:
        end = set()
        for subrule in rule:
            buff = {start}
            for r in subrule:
                temp = set()
                for l in buff:
                    temp.update(is_valid(r, message, l))
                buff = temp
            end.update(buff)
        return end


def solve_part_one():
    ans = 0

    for message in messages:
        valid = is_valid(0, message, 0)
        if len(message) in valid:
            ans += 1

    return ans


def solve_part_two():
    ans = 0
    formatted_rules[8] = [[42], [42, 8]]
    formatted_rules[11] = [[42, 31], [42, 11, 31]]

    for message in messages:
        valid = is_valid(0, message, 0)
        if len(message) in valid:
            ans += 1

    return ans


if __name__ == '__main__':
    print("p1:", solve_part_one())
    print("p2:", solve_part_two())
