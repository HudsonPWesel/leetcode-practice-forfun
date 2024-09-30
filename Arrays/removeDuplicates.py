def removeDuplicates(nums):
    l = 1
    res = 1
    for i in range(1, len(nums)):
        if nums[i - 1] != nums[i]:
            nums[l] = nums[i]
            res += 1
            l += 1
    print(nums)
    return res


print(removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
