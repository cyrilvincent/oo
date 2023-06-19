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

class Book:

# Créer le constructeur, les attributs
# net_price = price * 1.055
# tester

# Transformer net_price en property
# Créer la dataclass Author
# Créer la dataclass Publisher
# Tester

    def __init__(self, id: str,
                 title: str,
                 price: float,
                 date: datetime.datetime = datetime.datetime.now(),
                 nb_page: int = 0,
                 publisher: Publisher = Publisher("", ""),
                 authors: List[Author] = []):
        self.id = id
        self.title = title
        self.price = price
        self.date = date
        self.nb_page = nb_page
        self.publisher = publisher
        self.authors = authors

    @property
    def net_price(self):
        return self.price * 1.055

b1 = Book("001", "Python", 10)
print(b1)
print(f"Book price: {b1.net_price:.2f}")
b2 = Book("002", "Numpy", 20, publisher=Publisher("123", "ENI"))
b2.price+=1
print(b2.price)
print(b2)

print(b1.net_price)
# <=>
# print(Book.net_price(b1))

a1 = Author("Victor", "Hugo")
print(a1)

b3 = Book("1234", "Les misérables", 5, authors=[a1])






