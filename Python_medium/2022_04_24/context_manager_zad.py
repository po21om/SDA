from time import time
from time import sleep

class MeasureTime:
    def __enter__(self):
        self.start_time = time()
        return self

    def __exit__(self, exec_type, exc_val, exc_tb):
        self.end_time = time()
        print(self.end_time-self.start_time)


if __name__ == '__main__':
    with MeasureTime() as mt:
        # for _ in range(100000):
        #     print("tralalalala")
        sleep(5)