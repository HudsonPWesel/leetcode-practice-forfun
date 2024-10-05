from typing import List


def searchInsert(nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1
    mdpt = None
    while l <= r:
        mdpt = (r + l) // 2
        if nums[mdpt] > target:
            r = mdpt - 1
        elif nums[mdpt] < target:
            l = mdpt + 1
        else:
            return mdpt
    print(nums)
    return l


print(searchInsert([1, 2, 3, 4], 0))
