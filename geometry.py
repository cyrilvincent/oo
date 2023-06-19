from dataclasses import dataclass


@dataclass
class Point:

    x: float
    y: float

    def move(self, x: float, y: float):
        self.x = x
        self.y = y



class Rectangle:

    def __init__(self, width: float, length: float, coord: Point=Point(0,0)):
        self.width = width
        self.length = length
        self.coord = coord


    @property
    def area(self):
        return self.width * self.length




r1 = Rectangle(3,2, Point(5,-2))
r1.coord.move(1,2)
print(r1.area)
