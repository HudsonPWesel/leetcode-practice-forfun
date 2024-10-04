def hasDuplicate(nums) -> bool:
    seen_nums = {}
    for num in nums:
        if num in seen_nums:
            return True
        else:
            seen_nums[num] = num

    return False


print(hasDuplicate([1, 2, 3, 4]))
print(hasDuplicate([1, 2, 2, 3]))
