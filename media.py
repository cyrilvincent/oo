# Créer la classe Book avec 5 à 10 attributs
# Créer le méthode net_price() price * 1.05
# Modifier la méthode get_net_price() en propriété
# Créer la classe Publisher avec un @dataclass : id, name, phone, mail
# Créer la class Author : id, first_name, last_name
# Créer une manière de compter les books en mémoire
# b1=None, b1 = b2, del(b1)
from dataclasses import dataclass

class Book:

    def __init__(self, id: str, title:str, price: float, type: str="", lang: str="fr-FR", nb_page:int=0):
        self.id = id
        self.title = title
        self.type = type
        self.nb_page = nb_page
        self.price = price
        self.lang = lang

    @property
    def net_price(self) -> float:
        return self.price * 1.05

    def __del__(self):
        pass

@dataclass
class Publisher:

    id: str
    name: str
    mail: str
    phone: str = ""

@dataclass
class Author:

    id: str
    first_name: str
    last_name: str

b1 = Book("1", "Python pour les nuls", 10, nb_page=99)
b2 = Book("2", "Numpy", 20)
print(b1.net_price)
print(b1.price, b2.price)

print(b1.net_price)
# print(Book.net_price(b1))

p1 = Publisher("1", "Havas", "a@a.a")
print(p1)



