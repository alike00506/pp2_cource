def squares(a,b):
    for i in range(b+1):
        yield i * i 

a = int(input())
b = int(input())
square_of_nmbrs = squares(a,b)
for squares in square_of_nmbrs :
    print(squares)
