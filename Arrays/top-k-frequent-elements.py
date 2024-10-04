from typing import List


def topKFrequent(nums: List[int], k: int) -> List[int]:
    res = {}
    count = [[] for i in range(len(nums) + 1)]
    final_res = []

    for num in nums:
        res[num] = res.get(num, 0) + 1
    for num, num_count in res.items():
        count[num_count].append(num)
    for i in range(len(count) - 1, 0, -1):
        for j in range(len(count[i])):
            if len(final_res) != k:
                final_res.append(count[i][j])
    return final_res


print(topKFrequent([1, 2, 3, 3, 3], 2))
