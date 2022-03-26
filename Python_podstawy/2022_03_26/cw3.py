from osoba import Osoba
from urzednik import Urzednik

ela = Osoba(name="Ela", sex=1)

jaro = Urzednik(name="Jaromir", sex=0, wydzial="Ministerstwo Głupich Kroków")

print(jaro.name, jaro.sex, jaro.age, jaro.wydzial)
print(jaro.whoami())
jaro.rozpatrz_wniosek()