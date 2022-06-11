# Napisz funkcję korzystającą z wyrażeń regularnych która z zadanego tekstu wyciągniw szystkie liczby.
#
# Input:
# "test43543lfdsfdsfl534543fdgl432fr"
# Output:
# 43543
# 534543
# 432

import re
test = "test43543lfdsfdsfl534543fdgl432fr"
result = re.findall(r'\d+', test)
print(result)

# 10:54
# Zadanie 2:
# Weź ten sam tekst, co w zadaniu wyżej i napisz program, używając wyrażeń regularnych,
# który usunie wszystkie cyfry z tekstu.

print(re.sub(r'\d', '', test))

# Zadanie 3:
# Napisz program, który używając wyrażeń regularnych, sprawdzi czy podany numer telefonu jest poprawny.
#
# Poprawne numery to:
#
# 48123456789
# +48123456789
# 0048123456789
# czyli na początku albo samo 48, albo +48 albo 0048 a potem 9 cyfr.

test2 = "48123456789 +48123456789 0048123456789 +4812345789 004812345 048123456789 -48123456789"
test3 = '-48123456789'
test2_list = test2.split()
# print(test2_list)
result2 = re.fullmatch(r'(\+48|0048|48)\d{9}',test3)
print(result2.group(0))