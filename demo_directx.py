import abc
import config

class APIMicrosoft(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def display(self, x:int, y:int):...

    @abc.abstractmethod
    def move(self, x: int, y: int):...

class NVidiaImpl(APIMicrosoft):

    def display(self, x:int, y:int):
        print(f"NVidia display ({x}, {y})")

    def move(self, x: int, y: int):
        print(f"NVidia move ({x}, {y})")

    def additional(self):
        print(f"NVidia additional")

class IntelImpl(APIMicrosoft):

    def display(self, x: int, y: int):
        print(f"Intel display ({x}, {y})")

    def move(self, x: int, y: int):
        print(f"Intel move ({x}, {y})")

if __name__ == '__main__':
    print(f"Version {config.version}")
    driver: APIMicrosoft = config.driver
    driver.display(3,2)
    driver.move(4,-1)
    # if type(driver) is NVidiaImpl:
    driver.additional()


