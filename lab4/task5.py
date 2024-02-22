# def sqr() :
#     global x
#     x = float(input())
#     y = x * x
#     return y
# result = sqr()
# print(result)


def generate_squares(N):
    for i in range(N):
        yield i**2


N = int(input())
squares_generator = generate_squares(N)


for square in squares_generator:
    print(square)
