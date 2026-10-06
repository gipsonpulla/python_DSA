from typing import *

def add(x: int, y: int) -> int:
    if not isinstance(x, int) or not isinstance(y, int):
        raise TypeError("x and y must be integers")
    total = x + y
    return total

#print (add(10, 20))

def add2(x: int, y: int) -> int:
    total = x + y
    return total

try:
    print (add2("10", 20))
except TypeError:
    print ("Only integers are allowed")