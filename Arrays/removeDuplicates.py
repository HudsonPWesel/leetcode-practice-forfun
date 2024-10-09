def removeDuplicates(nums):
    l = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[l] = nums[i]
            l += 1
    print(nums)


print(removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
