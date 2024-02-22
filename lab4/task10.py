import math
def degtorad(n):
   
    result = (n * math.pi) / 180 
    return result
n = float(input())
rad = degtorad(n)

print(rad)