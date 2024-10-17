from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    res = []

    for i, a in enumerate(nums):
        if i > 0 and a == nums[i - 1]:
            continue
        l, r = 0, len(nums) - 1
        while l < r:
            current = a + nums[l] + nums[r]

            if current > 0:
                r -= 1
            elif current < 0:
                l += 1
            else:
                res.append([a, nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
        return res
