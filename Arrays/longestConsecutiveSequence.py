from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        new_set = set(nums)
        longest = 0
        for n in nums:
            if (n - 1) not in new_set:
                length = 0
                while n + length in new_set:
                    length += 1
                longest = length if length > longest else longest
            else:
                continue
        return longest
