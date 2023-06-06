from dataclasses import dataclass

@dataclass
class Rectangle:

    length: float
    width: float

    # def __init__(self, length: float, width : float):
    #     self.length = length
    #     self.width = width

    @property
    def area(self):
        return self.length * self.width

r1 = Rectangle(3,2)
print(r1.area)