import abc
from typing import List

import repository
import media

class AbstractService(metaclass=abc.ABCMeta):

    def __init__(self):
        self.cart = media.Cart()
        # repo.load

    @abc.abstractmethod
    def search(self, keywords: str) -> List[media.Media]:...
    # Retourne repo.medias

    @abc.abstractmethod
    def get_details(self, id: str) -> media.Media:...

    @abc.abstractmethod
    def add_media_to_cart(self, m: media.Media):...

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





