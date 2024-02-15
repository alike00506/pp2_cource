def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

nums_input = input()
nums_list = list(map(int, nums_input.split()))

# Output the result
result = has_33(nums_list)
print(result)
