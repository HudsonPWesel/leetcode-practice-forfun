def hasDuplicate(nums) -> bool:
    seen_nums = {}
    for num in nums:
        if seen_nums.get(num, 0) > 0:
            return True
        seen_nums[num] = 1
    return False


print(hasDuplicate([1, 2, 3, 4]))
print(hasDuplicate([1, 2, 2, 3]))
