from typing import List

import media
import abc

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

class BookCsvRepository(AbstractRepository):
    pass

class BookXmlRepository(AbstractRepository):
    pass

class BookJsonRepository(AbstractRepository):
    pass

class BookXlRepository(AbstractRepository):
    pass

class BookPickleRepository(AbstractRepository):
    pass

