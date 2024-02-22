def even(n):
    for i in range(n):
        yield i * 2

n = int(input())
eventon = even(n)


result = ', '.join(map(str, eventon))

print(result)
