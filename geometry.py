class Rectangle:

    def __init__(self, width: float, length: float):
        self.width = width
        self.length = length

    @property
    def area(self):
        return self.width * self.length


r1 = Rectangle(3,2)
print(r1.area)
