
from typing import List


def twoSum(nums: List[int], target) -> List[int]:
    counterparts = {}
    for index, val in enumerate(nums):
        if (target - val) in counterparts.keys():
            return [index, counterparts[target - val]]
        counterparts[val] = index
    return []


print(twoSum([2, 7, 11, 15], 9))

