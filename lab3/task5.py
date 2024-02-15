def generate_permutations(input_str, current=''):
    if len(input_str) == 0:
        print(current)
    else:
        for i in range(len(input_str)):
            char = input_str[i]
            remaining_chars = input_str[:i] + input_str[i+1:]
            generate_permutations(remaining_chars, current + char)


user_input = input()
generate_permutations(user_input)
