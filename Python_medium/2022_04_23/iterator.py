from math import sqrt


class PrimeIterator:
    def __init__(self, n):
        self.n = n
        self.generated_numbers = 0
        self.number = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.number += 1
        if self.generated_numbers >= self.n:
            raise StopIteration
        elif self.is_prime(self.number):
            self.generated_numbers += 1
            return self.number
        return self.__next__()

    def is_prime(self, n):
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True


iterka = PrimeIterator(10000)

for elem in iterka:
    print(elem)
