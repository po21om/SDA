#Przygotować klasę bazową Zwierze z metodą daj_glos i 4 klasy pochodne:
# Pies ,Kot i 2 wymyślone zwierzęta. Następnie zaimplementować dla każdego zwierzęcia metodę daj_glos.
# Stworzyć listę z obiektami każdego zwierzęcia i w pętli wywować dla każdego metodę daj_glos.

from abc import ABC, abstractmethod


class Zwierze(ABC):

    @abstractmethod
    def daj_glos(self):
        pass


class Pies(Zwierze):

    def daj_glos(self):
        return 'Woof Woof'


class Kot(Zwierze):

    def daj_glos(self):
        return 'Miau'


class Kurczak(Zwierze):

    def daj_glos(self):
        return 'Pi Pi Pi'


class Zaba(Zwierze):

    def daj_glos(self):
        return 'Kum Kum'

lista_zwierzat = [Pies(), Kot(), Kurczak(), Zaba()]

for zwierze in lista_zwierzat:
    print(zwierze.daj_glos())