from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    last = (m + n) - 1
    while m > 0 and n > 0:
        if nums1[m - 1] > nums2[n - 1]:
            nums1[last] = nums1[m - 1]
            m -= 1
        else:
            nums1[last] = nums2[n - 1]
            n -= 1
        last -= 1
    while n > 0:
        nums1[last] = nums2[n]
        n, last = n - 1, last - 1


merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
