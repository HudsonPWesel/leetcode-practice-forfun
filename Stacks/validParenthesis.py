def isValid(s: str) -> bool:
    mappings = {'(': ')', '[': ']', '{': '}'}
    stack = []
    for c in s:
        if c not in mappings:
            if c in list(mappings.values()) and stack and mappings[stack[-1]] == c:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
    return len(stack) == 0


print(isValid("()"))
