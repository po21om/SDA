# Klasa = [["imie", [3 losowe oceny]]
# 3 uczniów z 3 ocenami
# średnia

import random

dziennik = [[name,[random.randint(1,6) for i in range(3)]] for name in ["Janek", "Aleks", "Zuzia"]]
suma_srednich = 0
for poz in dziennik:
    print(f"{poz[0]} posiada średnią {sum(poz[1])/len(poz[1]):.2f}")
    suma_srednich += sum(poz[1])/len(poz[1])


print(f"Średnia klasy {suma_srednich/len(dziennik):.2f}")

srednia = sum(sum(poz[1])/len(poz[1]) for poz in dziennik) / len(dziennik)
print(f"{(sum(sum(poz[1])/len(poz[1]) for poz in dziennik) / len(dziennik)):.2f}")


