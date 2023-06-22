from typing import List
import csv

import jsonpickle

import media
import abc
import pickle

class AbstractRepository(metaclass=abc.ABCMeta):

    def __init__(self, path: str):
        self.path = path
        self.medias: List[media.Media] = []

    def clear(self):
        self.medias = []

    def get_all(self) -> List[media.Media]:
        return self.medias

    def get_by_id(self, id: str) -> media.Media | None:
        for m in self.medias:
            if m.id == id:
                return m
        return None

    def get_by_title(self, title:str) -> List[media.Media]:
        res = []
        for m in self.medias:
            if title.upper() in m.title.upper():
                res.append(m)
        return res

    def get_by_price(self, price: float) -> List[media.Media]:
        res = []
        for m in self.medias:
            if m.price <= price:
                res.append(m)
        return res


    def add(self, m: media.Media):
        self.medias.append(m)

    def remove(self, m: media.Media):
        self.medias.remove(m)

    @abc.abstractmethod
    def load(self):...

    @abc.abstractmethod
    def save(self):...


class BookCSVRepository(AbstractRepository):

    def __init__(self, path: str):
        super().__init__(path)

    def load(self):
        with open(self.path, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                id = row["id"]
                title = row["title"]
                price = float(row["price"])
                b = media.Book(id, title, price)
                self.medias.append(b)

    def save(self):
        with open(self.path, "w") as f:
            f.write("id,title,price\n")
            for m in self.medias:
                f.write(f"{m.id},{m.title},{m.price}\n")

class BookPickleRepository(AbstractRepository):

    def __init__(self, path: str):
        super().__init__(path)

    def load(self):
        with open(self.path, "rb") as f:
            self.medias = pickle.load(f)

    def save(self):
        with open(self.path, "wb") as f:
            pickle.dump(self.medias, f)

