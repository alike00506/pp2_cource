def is_prime(num):
    if num < 2:
        return False 
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False  
    return True 

def filter_prime(numbers):
    prime_numbers = [] 
    for num in numbers:
        if is_prime(num):
            prime_numbers.append(num)  
    return prime_numbers


input_numbers = input()
numbers_list = [int(x) for x in input_numbers.split()]

result = filter_prime(numbers_list)
print( result)
