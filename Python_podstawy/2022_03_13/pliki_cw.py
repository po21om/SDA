# Funkcja która:
# Przyjmie z konsoli imię, nazwisko i wiek
# Losowo wygeneruje stan konta
# Zapisze dane do nowego pliku

import random as r
import uuid
def wniosek():
    imie, nazwisko, wiek = input("Podaj Imię: "), input ("Podaj nazwisko: "), input("Podaj wiek: ")
    stan_konta = r.randint(100,10000)
    with open(f"{uuid.uuid4()}.txt", "w", encoding="UTF-8") as b:
        b.write(f"{imie} {nazwisko} - {wiek} - Stan konta: {stan_konta} PLN")
wniosek()