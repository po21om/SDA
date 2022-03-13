import random
# powitanie
#
# imie = input("Wpisz imię: ")
# print(f"Cześć {imie}!")

# ocena - pochwala

# ocena = input("Podaj ocenę: ")
#
# if float(ocena) >= 4:
#     print("Dobra robota")
# elif float(ocena) >= 3:
#     print("Mogło być lepiej")
# else:
#     print("Do książek ... migiem")

# stworzenie postaci
# imie, wiek, zawód

print("Kreacja nowej postaci.")
# imie = input("Podaj imie: ")
# wiek = int(input("Podaj wiek: "))
zawod = input("Podaj zawód: ")
imie = "Thor"
wiek = 34
print(f"Witamy w nowym świecie {imie} w wieku {wiek} lat i zawodzie {zawod}.")
# zamów jedzenie
# nie obsługujemy zawodów na literę "L" albo konćżacych się na "el"

if zawod[:1].lower() == "l" or zawod[-2:].lower() == "el":
    print("Waszego rodzaju nie obsługujemy.")

    # Zaproponuj cos do picia do wyboru z: Wino, Piwo, Woda, Sok
    if wiek < 18:
        wybor = input("Mogę zaproponować Ci Wodę lub Sok. Co wybierasz? ")
        if wybor == "Sok" or wybor == "sok":
            print("Oto twój sok z gumijagód.")
        elif wybor == "Woda" or wybor == "woda":
            print("A oto i woda zwierzaku.")
        else:
            print("Wysłów się człowieku.")
    else:
        wybor = input("Mogę zaproponować Ci Wino, Piwo, Sok lub Wodę. Co wybierasz? ")
        if wybor == "Sok" or wybor == "sok":
            print("Oto twój sok z gumijagód.")
        elif wybor == "Woda" or wybor == "woda":
            print("A oto i woda zwierzaku.")
        elif wybor == "Piwo" or wybor == "piwo":
            print("Proszę oto i pański złocisty trunek .")
        elif wybor == "Wino" or wybor == "wino":
            print("Proszę wielmożnego Pana wino z południa.")
        else:
            print("Wysłów się człowieku.")

else:
    print("Podaję kartę i proszę o wybranie.")

# Poproś o numer telefonu
# Szanse 50/50


los = random.random()
if los >= 0.5:
    print("Jasne. Mój numer to 123456789")
else:
    print("Spadaj.")




