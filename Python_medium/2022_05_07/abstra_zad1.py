# Utwórz klasę zwierze
# Pola: nazwa, wiek, waga
# Metoda: przedstaw_sie wyświetlającą nazwę i wiek oraz metodę urodziny
# zwiększającą wiek zwierzęcia
# Utwórz klasy slon i lew dziedziczącą metodę przedstaw_sie
# Wykorzystując polimorfizm zwiększ wiek o 1 dla wszystkich zwierząt
# Podpowiedź: stwórz listę zwierząt oraz dodaj funkcję operującą na tej liście

# W naszym przykładzie cały czas jest pewien mankament:
# - nie ma sensu tworzyć instancji klasy Zwierze.
# - chcemy zakazać tworzenia instancji tej klasy
# - każdy gatunek zwierzęcia ma swoją nazwę.
# Gdyby umieć wprowadzić tę nazwę na poziomie klasy Zwierze (a przecież
# wtedy jeszcze jej nie znamy, gdyż ustali się ona dopiero podczas
# dziedziczenia), można by napisać raz a dobrze metodę przedstawiającą
# zwierzę, z użyciem nazwy gatunku, i to już w klasie bazowej.
# - Wprowadź nową metodę w klasie bazowej: nazwa_gatunku() i oznacz jako
# abstrakcyjną
# Oznacza to, że definiujemy w klasie bazowej taką metodę, której nie
# implementujemy, ale spodziewamy się, że klasy dziedziczące się tym zajmą

from abc import ABC,  abstractmethod


class Animal(ABC):
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def introduce(self):
        return f'My name is {self.name}, I am {self.age} and I am a(n) {self.species()}.'

    def birthday(self):
        self.age += 1

    @abstractmethod
    def species(self):
        pass


class Elephant(Animal):
    def species(self):
        return 'Elephant'


class Lion(Animal):
    def species(self):
        return 'Lion'


lwica = Lion('Julia', 23, 56)
slon = Elephant('Jurek', 14, 1507)
lew = Lion('Kamil', 6, 123)

animals = [lwica, slon, lew]
for a in animals:
    a.birthday()
    print(a.introduce())

