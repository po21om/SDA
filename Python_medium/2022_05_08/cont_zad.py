from time import time, sleep


class InProgressTime:
    def __init__(self, filename):
        self.filename = filename
        self.file = None

    def __enter__(self):
        self.start_time = time()
        self.file = open(self.filename, 'w')
        self.file.write('In Progress\n')

    def __exit__(self, exec_type, exc_val, exc_tb):
        self.end_time = time()
        self.file.write(f'{self.end_time-self.start_time}')
        self.file.close()


if __name__ == '__main__':
    with InProgressTime('test.txt') as f:
        sleep(1)
