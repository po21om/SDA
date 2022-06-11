import threading
import time


class ThreadWithReturnValue(threading.Thread):
    def __init__(self, target, args=(), kwargs=None):
        if kwargs is None:
            kwargs = {}
        self.target = target
        self.args = args
        self.kwargs = kwargs
        super().__init__()

    def run(self):
        self.result = self.target(*self.args, **self.kwargs)

    def join(self, timeout=None):
        super().join(timeout)
        return self.result


def print_cube(num):
    # Funkcja zwracająca trzecią potęgę liczby podanej jako parametr
    time.sleep(5)
    print(f"Cube: {num * num * num}")


def print_square(num):
    # Funkcja zwracająca kwadrat liczby podanej jako parametr
    time.sleep(5)
    return num * num


if __name__ == "__main__":
    # tworzenie wątków
    t1 = ThreadWithReturnValue(target=print_square, args=(10,))
    t2 = threading.Thread(target=print_cube, args=(10,))

    # uruchomienie wątków
    t1.start()
    t2.start()

    # czekanie z wykonaniem dalszego kodu, aż oba wątki się zakończą
    print(f't1: {t1.join()}')
    t2.join()

    print("Done!")