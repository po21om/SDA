from copy import copy, deepcopy
from abc import ABC, abstractmethod
from math import pi


class Figura(ABC):
    @abstractmethod
    def obwod(self):
        pass

    @abstractmethod
    def pole(self):
        pass


class Prostokat(Figura):
    def __init__(self, a:float, b:float):
        self.a = a
        self.b = b

    def obwod(self):
        return 2 * a + 2 * b

    def pole(self):
        return a * b

lista = [1, 2, 3, [4, 5]]
lista2 = copy(lista)
lista3 = deepcopy(lista)

print(lista, lista2, lista3)

lista[0] = 9
print(lista, lista2, lista3)

lista[3][0] = 8
print(lista, lista2, lista3)

