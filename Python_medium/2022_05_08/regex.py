import re

# search szuka pierwszego wystąpienia wyrażenia
macze = re.search(r"[A-Z]la", "ala Ola Ela")
print(macze.group(0))

# match szuka dopasowania do początku tekstu, trochę tak jak ^
macze_2 = re.match(r"[A-Z]la", "Ala Ola Ela")
print(macze_2.group(0))

# fullmatch sprawdza czy całe wyrażenie pasuje do wzorca, jeśli dodamy to cokolwiek do tekstu
# to fullmatch zwróci None
macze_3 = re.fullmatch(r"[A-Z]la", "Ela")
print(macze_3.group(0))

# findall zwraca wszystkie dopasowania jako pythonowa lista
matche_4 = re.findall(r".la", "Ola ala Ela")
print(matche_4)

# finditer działa tak samo jak findall ale zwraca iterator a nie listę
iter = re.finditer(r".la", "Ola ala Ela")
for elem in iter:
    print(elem.group(0))

# split dopasowuje wyrażenie regularne do tekstu a następnie używa tych dopasowań
# do podzielenia tekstu
print(re.split(r",|\.", "apple,pear,grapes,carrot.cabbage,veggies.fruit,yard"))


# sub podmienia w tekstcie wystąpienia wyrażenia na to co znajduje się
# w 2 argumencie
print(re.sub(r"[a-ż]{4}", "psa", "Ala ma kota"))
print(re.sub(r"[a-ż]{4}", "psa", "Ala ma kota i jeża"))

# subn działa jak sub tylko dodatkowo zwraca ilość podmian
print(re.subn(r"[a-ż]{4}", "psa", "Ala ma kota"))
print(re.subn(r"[a-ż]{4}", "psa", "Ala ma kota i jeża"))