# Stworzenie postaci
# Imie, wiek, zawód
# 1. Przyjąć imię, wiek, zawód z konsoli (input) i wypisać powitanie postaci
#Wprowadzanie danych
imie = "Tomek" # imie = input("Podaj imię postaci - ")
wiek = 20 # wiek = int(input("Podaj wiek postaci - "))
zawod = input("Podaj zawód postaci - ")
#Powitanie klienta
print(f"Witaj {imie}!, masz {wiek} lat i pracujesz jako {zawod}")

# LEKARZ, lekarz, lEkArZ, LeKarZ, LEKarz - EL, el, El, eL , el
# Nie obsługujemy zawodów na literę "L" ALBO kończących się na "el"
if zawod.lower()[0] == "l" or zawod.lower().endswith("el"):
    print("Barman: Pański zawód nie pozwala mi Pana obsłużyć")
else:
    # print("Barman: Co chciałby Pan zjeść?")
    # Zaproponuj coś do picia do wyboru z: WINO, PIWO, WODA, SOK
    # W zależności od wieku podaj napój lub odmów
    wybor = int(input("WYBIERZ: 1.WINO 2.PIWO 3.WODA 4.SOK    - "))
    if wybor == 1 or wybor == 2:
        if wiek >= 18:  # komentarz
            print("Barman: Jesteś pełnoletni, proszę to dla ciebie.")
        else:
            print("Barman: Nie mogę ci tego sprzedać!")
    elif wybor == 3 or wybor == 4:
        print("Barman: Proszę to dla ciebie.")
    else:
        print("Barman: Nie mam tego w barze...")
# Poproś o numer telefonu
# Szanse 50/50
import random
los = random.random()
print(los)
if los >= 0.5:
    print("Jasne. Mój numer to 123123123")
else:
    print("Spadaj.")