from dataclasses import dataclass


@dataclass
class Point:
    x: float
    y: float


@dataclass
class Rectangle:

    length: float
    width: float
    coord: Point = Point(0,0)

    # def __init__(self, length: float, width : float):
    #     self.length = length
    #     self.width = width

    @property
    def area(self):
        return self.length * self.width

r1 = Rectangle(3, 2)
print(r1.area)