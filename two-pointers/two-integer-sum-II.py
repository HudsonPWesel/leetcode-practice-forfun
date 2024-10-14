from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 1, len(numbers)

        while l < r:
            current_sum = numbers[l - 1] + numbers[r - 1]
            if current_sum == target:
                return [l, r]
            elif current_sum < target:
                l += 1
            else:
                r -= 1


sol = Solution()
print(sol.twoSum([-5, -3, 0, 2, 4, 6, 8], 5))
