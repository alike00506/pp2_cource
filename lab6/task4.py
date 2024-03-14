import time
import math

def delayed_square_root(number, milliseconds):
    time.sleep(milliseconds / 1000.0)
    return math.sqrt(number)
number = int(input())
milliseconds_delay = int(input("enter milliseconds: "))
result = delayed_square_root(number, milliseconds_delay)
print(f"Square root of {number} after {milliseconds_delay} milliseconds is {result}")
