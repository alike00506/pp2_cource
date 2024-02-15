def spy_game(nums):
    code = [0, 0, 7]
    index = 0

    for num in nums:
        if num == code[index]:
            index += 1
            if index == len(code):
                return True

    return False


nums_input = input()
nums_list = list(map(int, nums_input.split()))


result = spy_game(nums_list)
print(result)
