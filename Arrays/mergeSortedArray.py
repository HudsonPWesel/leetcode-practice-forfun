from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    i, j = 0, 0
    for i in range(len(nums1)):
        if i < m:
            if nums2[j] < nums1[i]:
                nums1[i] = nums2[j]
                j += 1
            else:
                continue
        else:
            nums1[i] = nums2[j]
            j += 1


merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
