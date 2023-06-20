import demo_module as dm
import math
import numpy as np

def my_func(a, b):
    return "Other function"

res = my_func(2,3)
print(res)
res = dm.my_func(2,3)
print(res)
