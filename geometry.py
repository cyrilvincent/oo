from dataclasses import dataclass


@dataclass
class Point:
    x: float
    y: float

@dataclass
class Point3d(Point):
    z: float


@dataclass
class Rectangle:

    length: float
    width: float
    coord: Point

    # def __init__(self, length: float, width : float):
    #     self.length = length
    #     self.width = width

    @property
    def area(self):
        return self.length * self.width

class Square(Rectangle):

    def __init__(self, side: float, coord:Point):
        # self.width = side
        # self.length = side
        # self.coord = coord
        super().__init__(side, side, coord)

class TriangleRectangle(Rectangle):

    @property
    def area(self):
        return super().area/2

r1 = Rectangle(3, 2, Point(0,0))
print(r1.area)

p3d = Point3d(1,2,3)

s1 = Square(3, Point(0,0))
print(s1.__dir__())