from typing import List


def sliding_window_max(nums: List[int], k: int) -> int:
    total = sum(nums[:k])
    max_total = total
    for i in range(len(nums) - k):
        total -= nums[i]
        total += nums[i + k]
        max_total = max(total, max_total)
    return max_total


print(sliding_window_max([1, 2, 3, 4, 5, 6], 3))
