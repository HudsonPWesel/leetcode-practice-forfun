from typing import List


def binarySearch(nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1
    while l < r:
        mdpt = (l + r) // 2

        if nums[mdpt] < target:
            l = mdpt + 1
        elif nums[mdpt] > target:
            r = mdpt - 1
        else:
            return mdpt
