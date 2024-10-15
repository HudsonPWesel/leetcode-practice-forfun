from typing import List


def maxProfit(prices: List[int]) -> int:
    l, r = (0, 1)
    max_total = 0
    for r in range(0, len(prices)):
        if prices[l] < prices[r]:
            max_total = max(max_total, prices[r] - prices[l])
        else:
            l = r
        r += 1
    return max_total


print(maxProfit([1, 2, 3, 4, 5, 6, 7]))
