# Zadanie z *
# Wypisać skład osobowy oraz średnią klasy
# o losowej zartości uczniów (max. 36)
# z losowymi ocenami (5-15) w skali szkolnej (1-6)


import random
imiona = ["Ania", "Bartek", "Tomek", "Piotrek", "Jacek", "Zuzia", "Ala", "Monika", "Michał", "Zosia", "Mikołaj"]
dziennik = [[(imiona[random.randint(0,10)]),[random.randint(1,6) for i in range(1,random.randrange(6,15))]] for num in range(1,random.randrange(2,36))]
suma_srednich = 0
# print(dziennik) # by sprwdzic prawidlowosc wygenerowanego dziennika
for poz in dziennik:
    print(f"{poz[0]} posiada średnią {sum(poz[1])/len(poz[1]):.2f}")

print(f"Średnia klasy składającej się z {len(dziennik)} osób, wynosi {(sum(sum(poz[1])/len(poz[1]) for poz in dziennik) / len(dziennik)):.2f}")
