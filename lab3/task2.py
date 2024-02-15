def centrigade():
    global x
    x = (5/9) * (float(x) - 32)
    return x
x = input()
# result = centrigade()
# print(result)
print(centrigade())