import abc
from typing import List

import config
import repository
import media

class AbstractService(metaclass=abc.ABCMeta):

    def __init__(self):
        self.cart = media.Cart()
        self.repo = config.default_repository
        self.repo.load()


    @abc.abstractmethod
    def search(self, keywords: str) -> List[media.Media]:...
    # Retourne repo.medias

    @abc.abstractmethod
    def get_details(self, id: str) -> media.Media:...

    @abc.abstractmethod
    def add_media_to_cart(self, m: media.Media):...

    @abc.abstractmethod
    def remove_media_from_cart(self, m: media.Media):...

    @abc.abstractmethod
    def get_cart(self):...

    @abc.abstractmethod
    def validate_cart(self) -> bool:...
    # vrai si > 0 media

    @abc.abstractmethod
    def pay(self):...
    # print("OK")

class MediaService(AbstractService):

    def __init__(self):
        super().__init__()

    def search(self, keywords: str) -> List[media.Media]:
        return self.repo.get_by_title(keywords)

    def get_details(self, id: str) -> media.Media:
        return self.repo.get_by_id(id)

    def add_media_to_cart(self, m: media.Media):
        self.cart.is_validate = False
        self.cart.add(m)

    def validate_cart(self) -> bool:
        if len(self.cart.medias) > 0:
            self.cart.is_validate = True
        else:
            self.cart.is_validate = False
        return self.cart.is_validate

    def remove_media_from_cart(self, m: media.Media):
        self.cart.remove(m)
        self.cart.is_validate = False

    def pay(self):
        if self.cart.is_validate:
            print("Pay")
        else:
            raise ValueError("Cannot pay the cart")

    def get_cart(self):
        return self.cart







