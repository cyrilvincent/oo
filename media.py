import datetime
from dataclasses import dataclass
from typing import List


@dataclass
class Author:

    first_name: str
    last_name: str

@dataclass
class Publisher:

    id: str
    name: str

class Media:

# Créer le constructeur, les attributs
# net_price = price * 1.055
# tester

# Transformer net_price en property
# Créer la dataclass Author
# Créer la dataclass Publisher
# Tester
    nb_media = 0

    def __init__(self, id: str,
                 title: str,
                 price: float,
                 date: datetime.datetime = datetime.datetime.now(),
                 publisher: Publisher = Publisher("", ""),
                 authors: List[Author] = []):
        self.id = id
        self.title = title
        self.price = price
        self.date = date
        self.publisher = publisher
        self.authors = authors
        Media.nb_media += 1

    @property
    def net_price(self):
        return self.price * 1.2

    def __del__(self):
        Media.nb_media -= 1

    def __repr__(self):
        return f"Media: {self.id} {self.title} {self.price}"

class Book(Media):

    nb_book = 0

    def __init__(self, id: str,
                 title: str,
                 price: float,
                 date: datetime.datetime = datetime.datetime.now(),
                 publisher: Publisher = Publisher("", ""),
                 authors: List[Author] = [],
                 nb_page = 0
                 ):
        super().__init__(id, title,price,date,publisher,authors)
        self.nb_page = nb_page
        Book.nb_book += 1

    def net_price(self):
        return self.price * 1.055

    def __del__(self):
        super().__del__()
        Book.nb_book -= 1

class Cd(Media):

    def __init__(self, id: str,
                 title: str,
                 price: float,
                 date: datetime.datetime = datetime.datetime.now(),
                 publisher: Publisher = Publisher("", ""),
                 authors: List[Author] = [],
                 nb_track = 0
                 ):
        super().__init__(id, title,price,date,publisher,authors)
        self.nb_track = nb_track

b1 = Book("001", "Python", 10)
print(b1)
print(f"Book price: {b1.net_price}")
b2 = Book("002", "Numpy", 20, publisher=Publisher("123", "ENI"))
b2.price+=1
print(b2.price)
print(b2)

print(b1.net_price)
# <=>
# print(Book.net_price(b1))

a1 = Author("Victor", "Hugo")
print(a1)

b3 = Book("1234", "Les misérables", 5, authors=[])
b3.authors.append(Author("toto", "titi"))

print(f"Nb media: {Media.nb_media}")
del b3
print(f"Nb media: {Media.nb_media}")

cd1 = Cd("0014", "Johnny", 10, nb_track=9)
print(cd1)






