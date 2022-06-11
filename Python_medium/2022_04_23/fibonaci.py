class FibonacciIterator:
    def __init__(self, n):
        self.n = n
        self.a = 1
        self.b = 1
        self.number = 0
    def __iter__(self):
        return self

    def __next__(self):
        self.number += 1
        if self.number > self.n:
            raise StopIteration
        self.a, self.b = self.b , (self.a + self.b)
        return self.b

fibo = FibonacciIterator(10)

for elem in fibo:
    print(elem)
