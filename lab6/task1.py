from functools import reduce

def multiply_list(numbers):
    if not numbers:
        return None  
    else:
        product = reduce(lambda x, y: x * y, numbers)
        return product
my_numbers = [2, 3, 4, 5]
result = multiply_list(my_numbers)
print(result)
