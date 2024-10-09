from typing import List


def binary_search(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        mdpt = (l + r) // 2
        if nums[mdpt] > target:
            r = mdpt - 1
        elif nums[mdpt] < target:
            l = mdpt + 1
        else:
            return mdpt
    return -1


print(binary_search([1, 2, 3, 4], 4))
print(binary_search([1, 2, 3, 4], 14))
