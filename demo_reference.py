# Value type
a = 1
b = a
a += 1
print(a, b)

# Reference type
l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l1, l2)

# Clone
l1 = [1, 2, 3]
l2 = list(l1)
l1.append(4)
print(l1, l2)

# == vs is
l1 = [1, 2, 3]
l2 = [1, 2, 3]
print(l1 == l2, l1 is l2)
l1 = l2
print(l1 == l2, l1 is l2)