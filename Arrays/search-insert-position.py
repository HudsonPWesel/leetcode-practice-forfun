def searchInsert(self, nums: List[int], target: int) -> int:
    l, r = 0, len(nums)

    while l <= r:
        mdpt = int((l + r) / 2)
        if target == nums[mdpt]:
            return mdpt
        if mdpt > target:
            l = mdpt + 1
        else:
            r = mdpt - 1
    return l
