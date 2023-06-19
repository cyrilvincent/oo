print("Hello")

def add(i: float,j: float) -> float:
    return i + j

add_lambda = lambda x, y: x + y

toto = add
print(toto)
x = add_lambda(3, 3.14)
print(x)