import math


def x3(x):
    return x * 3

is_even = lambda x: x % 2 == 0

def is_prime(x):
    if x < 2:
        return False
    for div in range(2, int(math.sqrt(x)) + 1):
        if x % div == 0:
            return False
    return True

def my_filter(fn, l):
    res = []
    for x in l:
        if fn(x):
            res.append(x)
    return res

def yield_filter(fn, l):
    for x in l:
        if fn(x):
            yield x

def infinite_list():
    i = 0
    while True:
        yield i
        i += 1


my_list = list(range(100))

result = list(map(x3, my_list))
print(result)
result = list(filter(is_even, my_list))
print(result)

print([x * 3 for x in my_list])
print([x for x in my_list if x % 2 == 0])

print([x for x in my_list if is_prime(x)])
print(my_filter(is_prime, my_list))
# print(list(yield_filter(is_prime, my_list)))

# res = infinite_list()
res = yield_filter(is_prime, infinite_list())
res2 = yield_filter(is_even, res)
# print(len(infinite_list()))
# for x in res2:
#     print(x)

res = (x for x in my_list if is_prime(x))
for x in res:
    print(x)

res = list((x for x in my_list if is_prime(x)))