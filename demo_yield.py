from typing import List

def is_prime(i: int) -> bool:
    if i < 2:
        return False
    for div in range(2, i):
        if i % div == 0:
            return False
    return True

def filter_even(l: List[int]) -> List[int]:
    res = []
    for i in l:
        if i % 2 == 0:
            res.append(i)
    return res

def filter_prime(l: List[int]) -> List[int]:
    res = []
    for i in l:
        if is_prime(i):
            res.append(i)
    return res

def filter2(fn, l):
    res = []
    for i in l:
        if fn(i):
            res.append(i)
    return res

def map2(fn, l):
    res = []
    for i in l:
        res.append(fn(i))
    return res

l1 = list(range(100))
print(filter2(lambda x: x % 2 == 0, l1))
print(filter2(is_prime, l1))
print(list(filter(lambda x: x % 2 == 0, l1)))
print(list(filter(is_prime, l1))) # <=> intention list

print(list(map(lambda x: x ** 2, l1)))



def filter(fn, l):
    for i in l:
        if fn(i):
            yield i

def map(fn, l):
    for i in l:
        yield fn(i)

def my_range(nb):
    i = 0
    while i < nb:
        yield i
        i += 1

# Redéfinir les méthodes == et != dans media et tester
# Dans un cart récupérer le __dict__
# Essayer de porter le repository.load en générateur


def infinite():
    i = 0
    while True:
        yield i
        i += 1

# l2 = my_range(1000000000000000000000000000000000000000000000000000000000000000000)
l2 = infinite()
res = filter(lambda x: x % 2 == 0, l2)
res = filter(is_prime, res)
res = map(lambda x: x ** 2, res)
for x in res:
    print(x)

# filter + map = generator
res = (x ** 2 for x in l2 if x % 2 == 0)
print(res)
# print(len(res))
for x in res:
    print(x)

# l3 = range(100)
# res = list((x ** 2 for x in l2 if x % 2 == 0))
# # <=>
# res = [x ** 2 for x in l2 if x % 2 == 0]

