def reversnum(n):
    while n != -1 :
        yield n
        n = n -1 

n = int(input())
revnums = reversnum(n)
for nums in revnums:
    print(nums)