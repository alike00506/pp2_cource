import math
def areaofpolygon(n,a):
    y = a/(2*math.tan(math.pi/n))
    area = n * a * y /2
    return area
n = int(input())
a = int(input())
areapol = areaofpolygon(n,a)
print(math.ceil(areapol))