from dataclasses import dataclass


@dataclass
class Point:

    x: float
    y: float

    def move(self, x: float, y: float):
        self.x = x
        self.y = y

@dataclass
class Point3d(Point):

    z: float



class Rectangle:

    def __init__(self, width: float, length: float, coord: Point=Point(0,0)):
        self.width = width
        self.length = length
        self.coord = coord


    @property
    def area(self):
        return self.width * self.length

    def __repr__(self):
        return f"Rectangle: {self.width}x{self.length}"

class Square(Rectangle):

    def __init__(self, side: float, coord: Point=Point(0,0)):
        super().__init__(side, side, coord)

class TriangleRectangle(Rectangle):

    def __init__(self, width: float, length: float, coord: Point = Point(0, 0)):
        super().__init__(width, length, coord)

    @property
    def area(self):
        return super().area / 2




# r1 = Rectangle(3,2, Point(5,-2))
# r1.coord.move(1,2)
# print(r1.area)
# p3d = Point3d(1,2,3)
# print(r1)
