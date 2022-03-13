# 5 uczniów
# 10 losowych ocen (1-6)
# Promocja wymaga średniej 3.54
# Wypisać osoby które zdały i które nie zdały

import random

uczniowie = {"Janek":[], "Ala":[], "Monika":[], "Stefan":[], "Aga":[]}

for uczen in uczniowie:
    while uczen.() < 6:
        uczniowie.append(random.randint(1,6))

print(uczniowie)