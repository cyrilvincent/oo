from typing import List
import math

l1 = range(100)

def positive_sinus(x: float) -> bool:
    return math.sin(x) > 0

def is_even(x: int) -> bool:
    return x % 2 == 0

def is_prime(x: int) -> bool:
    if x < 2:
        return False
    for div in range(2, x):
        if x % div == 0:
            return False
    return True


def filter_generic(l: List[int], fn) -> List[int]:
    res = []
    for x in l:
        if fn(x):
            res.append(x)
    return res

x = filter_generic(l1, is_even)
print(x)
x = filter_generic(l1, positive_sinus)
print(x)
x = filter_generic(l1, is_prime)
print(x)

print(4 % 2) # => 0
print(5 % 2) # => 1