# Przyjmij 3 oceny ucznia
# Policzyć średnią
# Dla średniej > 4: ustawić flagę stypendium na True
# Dla stypendysty wygenerować losową wysokość stypendium w przedziale 400-600 PLN00
import random

oceny = []
oceny.append(int(input("Podaj ocenę: ")))
oceny.append(int(input("Podaj ocenę: ")))
oceny.append(int(input("Podaj ocenę: ")))
srednia = sum(oceny)/len(oceny)
stypendium = None
if srednia > 4:
    stypendium = True
else:
    stypendium = False
if stypendium:
    print(f"Uczeń zdobył stypendium o wysokości {random.randint(400,600)} zł. Gratulacje.")
