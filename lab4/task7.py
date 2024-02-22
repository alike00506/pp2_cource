def divisible_by3and4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i


n = int(input())
divisible_numbers = divisible_by3and4(n)

for number in divisible_numbers:
    print(number)
