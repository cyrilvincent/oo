import media

def add(a, b):
    return a + b

def increment_price(self: media.Book):
    return self.price + 1

book = media.Book("1", "Python", 10, None)
print(book.__getattribute__("title"))
book.__setattr__("toto",12)
print(book.toto)
book.__setattr__("add", add)
print(book.add(1,2))

print(book.__dict__)
print(book.__dict__["title"])
book.__dict__["title"]="toto"
book.__dict__["toto"] = 13


