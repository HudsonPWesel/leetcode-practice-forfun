from typing import List


def topKFrequent(nums: List[int], k: int) -> List[int]:
    nums_count = {}
    order = []
    largest_key = nums[0]
    if k == 1:
        return [nums]
    for i in nums:
        nums_count[i] = nums_count.get(i, 0) + 1
        largest_key = i if nums_count[i] > nums_count[largest_key] else largest_key
        if nums_count[i] == 1:
            order.append(i)
        if len(order) == k:
            return order


print(topKFrequent([1, 2], 2))
