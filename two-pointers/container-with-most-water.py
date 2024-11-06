from typing import List


def maxArea(self, height: List[int]) -> int:
    l, r = 0, len(height) - 1
    current_max = 0
    while l < r:
        current_height = min(height[l], height[r])
        width = r - l
        current_max = max(current_max, current_height * width)
        if current_height == height[l]:
            l += 1
        else:
            r -= 1
    return current_max
