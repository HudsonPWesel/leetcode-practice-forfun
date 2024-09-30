def removeDuplicates(nums):
    for i in range(len(nums)):
        if nums[i] == i + 1 or (nums[i] == 0 and i == 0):
            continue
        else:
            if not (nums[-1] - i):
                nums[i] = nums[-1]
                print(nums)
                return i + 1
            else:
                nums[i] = i


print(removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
