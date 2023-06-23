import threading
import time

class MyThread(threading.Thread):

    def __init__(self, num, sleep, end_cb, step, progress_cb):
        super().__init__()
        self.num = num
        self.sleep = sleep
        self.result = 1
        self.end_cb = end_cb
        self.step = step
        self.progress_cb = progress_cb

    def run(self) -> None:
        for i in range(self.step):
            print(f"Hello {self.num}: {self.result}")
            self.result *= 2
            time.sleep(self.sleep)
            self.progress_cb(self.num, i / self.step)
        self.end_cb(self.result, self.num)

def main_end_callback(result, num):
    print(f"Result from {num}: {result}")

def main_progress_callback(num, progress):
    print(f"Progress from {num}: {progress * 100:.0f}%")


if __name__ == '__main__':
    t1 = MyThread(1, 0.5, main_end_callback, 20, main_progress_callback)
    t2 = MyThread(2, 0.75, main_end_callback, 15, main_progress_callback)
    t1.start()
    t2.start()
