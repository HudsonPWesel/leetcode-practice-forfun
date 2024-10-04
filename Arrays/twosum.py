
from typing import List


def twoSum(nums: List[int], target) -> List[int]:
    counterparts = {}
    for i in range(len(nums)):
        if abs(target - nums[i]) in counterparts:
            return [counterparts[target - nums[i]], 1]
        else:
            counterparts[nums[i]] = i
    return []


print(twoSum([2, 7, 11, 15], 9))
