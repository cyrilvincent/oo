import abc

class MyAbstractClass(metaclass=abc.ABCMeta):

    def __init__(self, x):
        self._x = x

    @abc.abstractmethod
    def increment(self):...

    @property
    @abc.abstractmethod
    def x(self):...

class Implementation(MyAbstractClass):

    def __init__(self, x):
        super().__init__(x)

    def increment(self):
        self._x += 1

    @property
    def x(self):
        return x

if __name__ == '__main__':
    # x = MyAbstractClass(0)
    x = Implementation(0)




