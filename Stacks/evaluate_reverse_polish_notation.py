from typing import List


def evalRPN(tokens: List[str]) -> int:
    nums = []
    operators = {'+': lambda x, y: x + y, '-': lambda x, y: x -
                 y, '*': lambda x, y: x * y, '/': lambda x, y: x // y}
    i = 0
    res = None
    if len(tokens) == 1:
        return int(tokens[0])
    for i in range(len(tokens)):
        if tokens[i] in operators:
            r = int(nums.pop(-1))
            l = int(nums.pop(-1))
            res = operators.get(tokens[i])(l, r)
            nums.append(res)
        else:
            nums.append(tokens[i])
        i += 1
    return res


print(evalRPN(['-1']))
