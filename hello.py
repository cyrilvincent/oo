def add(i, j):
    """
    Cette fonction add 2 nombres
    :param i: i
    :param j: j
    :return: i+j
    """
    return i + j



def is_even(i):
    if i % 2==0:
        return True
    else:
        return False

def is_even2(i):
    return i % 2 == 0

def factorielle(n: int) -> int:
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res



print("Hello World")
res = add(2,3)
print(is_even(3))
print(factorielle(4))
toto = add
print(toto(2,3))
print(res)