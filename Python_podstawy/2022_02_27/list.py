# oceny = []
# lista = ["Janek", 5, False]
# print(len(lista))
# print(lista)
# lista.append("Tomek")
# print(lista)

# przyjmij trzy oceny dla jednego ucznia
# wypisz srednia

# oceny.append(int(input("Podaj ocenę: ")))
# oceny.append(int(input("Podaj ocenę: ")))
# oceny.append(int(input("Podaj ocenę: ")))
#
# print(f"Średnia ocen: {(oceny[0]+oceny[1]+oceny[2])/len(oceny)}")

# alphabet = ["a", "b", "c", "d"]
# print(alphabet)
# alphabet.extend(["e", "f", "g", "h"])
# print(alphabet)

# owoce = ["jabłko", "banan", "ananas"]
# print(owoce)
# owoce.sort()
# print(owoce)

# lista uczniów same imiona i wyswietlic posortowane alphabetycznie

# uczniowie = ["Janek", "Zosia", "Ala", "Marysia", "Mikołaj", "Aleksander"]
# print(uczniowie)
# uczniowie.sort()
# print(uczniowie)
#
# uczniowie2 = [["Janek", 3], ["Zosia", 2], ["Ala", 1]]
# print(uczniowie2)
# uczniowie2.sort()
# print(uczniowie2)

# sorotowanie do nowej listy bez zmiany oryginalnej
import copyreg
#
# a = ["banan", "ananas"]
# print(a)
# b = sorted(a)
# print(a)
# print(b)
#
# print(a.index("ananas"))
# print(a[1])
#
# print(a.count("ananas"))
#
# num1 = [2, 3]
# num2 = [1, 4]
# print(sorted(num1+num2))

# czyszczenie list
# a.clear()
# print(a)

# kopia listy
# c = a.copy()
# print(a, b, c)

#wyciaga element z listy i zniej go usuwa (bez indexu ostatni element)
# print (c.pop())
# print(c)


liczby = [2,25,54,2,12,57,23,7]
print(liczby)
liczby.reverse()
print(liczby)
liczby.sort()
print(liczby)
print(liczby.pop())
print(liczby)
liczby.remove(2)
print(liczby)
liczby.reverse()
print(liczby)
