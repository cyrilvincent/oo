from dataclasses import dataclass
import abc


@dataclass
class Point:
    x: float
    y: float

@dataclass
class Point3d(Point):
    z: float

@dataclass
class Polygon(metaclass=abc.ABCMeta):

    coord: Point

    @property
    @abc.abstractmethod
    def area(self):...

@dataclass
class Losange(Polygon):

    def area(self):
        pass

@dataclass
class Rectangle(Polygon):

    length: float
    width: float

    # def __init__(self, length: float, width : float):
    #     self.length = length
    #     self.width = width

    @property
    def area(self):
        return self.length * self.width

    @property
    def perimeter(self):
        return 2 * (self.length + self.width)

class Square(Rectangle):

    def __init__(self, side: float, coord:Point):
        # self.width = side
        # self.length = side
        # self.coord = coord
        super().__init__(coord, side, side)

class TriangleRectangle(Rectangle):

    @property
    def area(self):
        return super().area/2

