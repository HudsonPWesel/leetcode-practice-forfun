from typing import List


def plusOne(digits: List[int]) -> List[int]:
    carry, i = 1, len(digits) - 1
    while carry:
        if i > -1:
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                carry = 0
        else:
            digits.insert(0, 1)
            carry = 0
        i -= 1
    return digits[::-1]


print(plusOne([9, 9, 9]))
