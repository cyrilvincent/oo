# Créer la classe Book avec 5 à 10 attributs
# Créer le méthode net_price() price * 1.05
# Modifier la méthode get_net_price() en propriété
# Créer la classe Publisher avec un @dataclass : id, name, phone, mail
# Créer la class Author : id, first_name, last_name
# Créer une manière de compter les books en mémoire
# b1=None, b1 = b2, del(b1)
from dataclasses import dataclass
from typing import List, Optional
import abc


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

class Media(metaclass=abc.ABCMeta):

    nb = 0

    def __init__(self, id: str, title:str, price: float, publisher: Publisher, type: str="", lang: str="fr-FR", authors: List[Author]=[]):
        self.id = id
        self.title = title
        self.type = type
        self.price = price
        self.lang = lang
        self.publisher = publisher
        self.authors = authors

        Media.nb += 1

    @property
    @abc.abstractmethod
    def net_price(self) -> float:...

    def __del__(self):
        Media.nb -= 1

    def __repr__(self):
        return f"Media {self.title} price: {self.price}€"

class Book(Media):

    def __init__(self, id: str, title: str, price: float, publisher: Optional[Publisher], type: str = "", lang: str = "fr-FR",
                 authors: List[Author] = [], nb_page: int = 0):
        super().__init__(id,title,price,publisher,type,lang,authors)
        self.nb_page = nb_page

    @property
    def net_price(self) -> float:
        return self.price * 1.05 * 0.95 + 0.01

class Cd(Media):

    def __init__(self, id: str, title: str, price: float, publisher: Publisher|None, type: str = "", lang: str = "fr-FR",
                 authors: List[Author] = [], nb_track: int = 0):
        super().__init__(id,title,price,publisher,type,lang,authors)
        self.nb_track = nb_track

    @property
    def net_price(self) -> float:
        return self.price * 1.05 * 0.8

@dataclass
class Cart:

    medias: List[Media]

    @property
    def price(self):
        sum = 0
        for media in self.medias:
            sum += media.price
        return sum

    @property
    def net_price(self):
        sum = 0
        for media in self.medias:
            sum += media.net_price
        return sum

    def add(self, media: Media):
        self.medias.append(media)

class Singleton:

    singleton: Cart = None

    def __init__(self):
        raise ValueError

    @staticmethod
    def get_instance():
        if Singleton.singleton is None:
            Singleton.singleton = Cart([])
        return Singleton.singleton





if __name__ == '__main__':
    b1 = Book("1", "Python pour les nuls", 10, Publisher("1","ENI","a@a.a"), nb_page=99, authors=[Author("02", "auteur1", "auteur1")])
    p1 = Publisher("1", "Havas", "a@a.a")
    my_authors = [Author("03", "author3", "author3"), Author("04", "author4", "author4")]
    b2 = Book("2", "Numpy", 20, p1, authors=my_authors)
    print(b1)
    print(b1.net_price)
    print(b1.price, b2.price)
    print(Book.nb)
    print(Book.nb)
    print(b1.publisher.name)
    print(b1.authors[0].last_name)
    print(len(b2.authors))


    print(b1.net_price)
    # print(Book.net_price(b1))
    del b2
    print(p1)

    print(b1)
    print(p1)

    cd1 = Cd("JH1", "Johnny Best Of", 10, None)



