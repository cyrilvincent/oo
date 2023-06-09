import threading
import time


class MyThread(threading.Thread):

    def __init__(self, name, nb_iteration, nb_sleep, fn_end_cb, fn_progress_cb):
        super().__init__()
        self.nb_iteration = nb_iteration
        self.name = name
        self.nb_sleep = nb_sleep
        self.result = 1
        self.fn_end_cb = fn_end_cb
        self.fn_progress_cb = fn_progress_cb

    def run(self) -> None:
        for i in range(self.nb_iteration):
            self.result *= 2
            # print(f"Thread {self.name}: {self.result}")
            time.sleep(self.nb_sleep)
            self.fn_progress_cb(i / self.nb_iteration, self.result, self.name)
        self.fn_end_cb(self.result)

def my_end_cb(result):
    print(f"Final result: {result}")

def my_progress_cb(completion: float, result: int, name: str):
    print(f"{name} progress {completion*100}%: {result}")

if __name__ == '__main__':
    thread1 = MyThread("Thread1", 10, 0.2, my_end_cb, my_progress_cb)
    thread2 = MyThread("Thread2", 20, 0.1, my_end_cb, my_progress_cb)
    thread3 = MyThread("Thread3", 20, 0.33, my_end_cb, my_progress_cb)
    thread1.start()
    thread2.start()
    thread3.start()
    result = thread1.result
    print(f"Result: {result}")