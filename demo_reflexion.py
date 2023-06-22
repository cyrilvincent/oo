import media

b = media.Book("001", "Python", 10)
print(b.title)
print(b.__getattribute__("title"))
print(b.__dict__)
print(b.__dict__["title"])
b.__dict__["title"] = "toto"
print(b.title)

b1 = media.Book("001", "Python", 10)
b2 = media.Book("001", "Python", 10)
print(b1 is b2)
print(b1 == b2)

l1 = list(range(100))

res = []
for i in l1:
    if i % 2 == 0:
        res.append(i)
print(res)

res = [x for x in l1 if x % 2 == 0]
print(res)

res = []
for i in l1:
    res.append(i ** 2)
print(res)

res = [x ** 2 for x in l1]
print(res)

res = [x ** 2 for x in l1 if x % 2 == 0]
print(res)
