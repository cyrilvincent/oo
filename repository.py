from typing import List

import media

class BookCSVRepository:

    def __init__(self, path: str):
        self.path = path
        self.medias: List[media.Media] = []

    def load(self):
        pass

    def clear(self):
        self.medias = []

    def get_all(self) -> List[media.Media]:
        return self.medias

    def get_by_id(self, id: str):
        pass

    # get_by_price get_by_title

    def add(self, m: media.Media):
        pass

    # remove
    def save(self):
        pass

    # TP : Porter loadCSV et saveCSV dans le repository
    # 2 : Idem pour BookPickleRepository, BookJSONRepo, BookXMLRepo
    # 3 : Tester, par exemple loadCSV -> saveJSON

