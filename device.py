from dataclasses import dataclass
import abc
from typing import List


@dataclass
class Mesure:
    timestamp:int
    value:float

class Device(metaclass=abc.ABCMeta):

    def __init__(self):
        self.mesures = []

    @abc.abstractmethod
    def start(self, nb_mesure: int):...

class Service:

    def __init__(self, device: Device):
        self.device = device

    def start(self, nb_mesure:int):
        self.device.mesures = []
        self.device.start(nb_mesure)

class Voltmetre(Device, metaclass=abc.ABCMeta):

    def __init__(self):
        super().__init__()
        self.count = 0

    @abc.abstractmethod
    def start(self, nb_mesure: int):...

class VoltmetreMock(Voltmetre):

    def start(self, nb_mesure: int):
        for i in range(nb_mesure):
            self.mesures.append(Mesure(i,i))


class VoltmetreMockB(Voltmetre):

    def start(self, nb_mesure: int):
        for i in range(nb_mesure):
            self.mesures.append(Mesure(i, i/100))






