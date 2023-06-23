import threading
import time

class MyThread(threading.Thread):

    def __init__(self, num, sleep):
        super().__init__()
        self.num = num
        self.sleep = sleep

    def run(self) -> None:
        for i in range(20):
            print(f"Hello {self.num}: {i}")
            time.sleep(self.sleep)

if __name__ == '__main__':
    t1 = MyThread(1, 0.5)
    t2 = MyThread(2, 0.75)
    t1.start()
    t2.start()