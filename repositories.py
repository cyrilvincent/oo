import pickle
from typing import List

import media
import abc
import csv

class AbstractRepository(metaclass=abc.ABCMeta):

    def __init__(self, uri: str):
        self.uri = uri
        self.medias:List[media.Media] = []

    @abc.abstractmethod
    def load(self):...

    @abc.abstractmethod
    def get_all(self) -> List[media.Media]:...

    @abc.abstractmethod
    def get_by_id(self, id: str) -> media.Media | None:...

    @abc.abstractmethod
    def get_by_title(self, title: str) -> List[media.Media]:...

    @abc.abstractmethod
    def get_by_price(self, price: float) -> List[media.Media]:...

    @abc.abstractmethod
    def save(self):...

    @abc.abstractmethod
    def save_as(self, uri: str):...

    @abc.abstractmethod
    def create(self, media: media.Media):...

    @abc.abstractmethod
    def update(self, media: media.Media): ...

    @abc.abstractmethod
    def delete(self, media: media.Media): ...

class BookGenericRepository(AbstractRepository, metaclass=abc.ABCMeta):

    def get_all(self) -> List[media.Media]:
        return self.medias

    def get_by_id(self, id: str) -> media.Media | None:
        for m in self.medias:
            if m.id == id:
                return m
        return None

    def get_by_price(self, price: float) -> List[media.Media]:
        pass

    def get_by_title(self, title: str) -> List[media.Media]:
        pass

    def create(self, media: media.Media):
        self.medias.append(media)

    def delete(self, media: media.Media):
        self.medias.remove(media)

    def update(self, media: media.Media):
        m = self.get_by_id(media.id)
        self.delete(m)
        self.create(media)


class BookCsvRepository(BookGenericRepository):

    def load(self):
        with open(self.uri) as f:
            reader = csv.DictReader(f)
            for row in reader:
                id = row["id"]
                title = row["title"]
                price = float(row["price"])
                book = media.Book(id, title, price, None)
                self.medias.append(book)


    def save(self):
        self.save_as(self.uri)

    def save_as(self, uri: str):
        with open(uri, "w") as f:
            writer = csv.DictWriter(f,["id", "title", "price"])
            for m in self.medias:
                writer.writerow({"id":m.id, "title":m.title, "price":m.price})



class BookXmlRepository(AbstractRepository):
    pass

class BookJsonRepository(AbstractRepository):
    pass

class BookXlRepository(AbstractRepository):
    pass

class BookPickleRepository(AbstractRepository):

    def save(self):
        with open(self.uri, "wb") as f:
            pickle.dump(self.medias, f)

    def load(self):
        with open(self.uri, "rb") as f:
            self.medias = pickle.load(f)

