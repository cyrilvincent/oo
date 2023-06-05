a = 1
b = a
a += 1
print(a, b)

x = [1, 2]
y = x
x.append(3)
print(x, y)
print(x == y, x is y)

n = [1, 2]
m = list(n)
n.append(3)
print(n, m)
print(n == m, n is m)

g = [1, 2]
h = [1, 2]
print(g == h, g is h)