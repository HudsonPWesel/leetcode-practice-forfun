def removeDuplicates(nums):
    res = 1
    for i in range(len(nums)):
        if nums[i] == i + 1:
            res += 1
            continue
        else:
            if not (nums[-1] - nums[i]):
                return res
            else:
                nums[i] = nums[i] + 1
    print(nums)
    return res


print(removeDuplicates([1, 1, 2]))
