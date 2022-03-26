from osoba import Osoba

ela = Osoba(name="Ela", sex=1)
michal = Osoba(name="Michał", sex=0)

print(ela.name, ela.sex, ela.age)
print(michal.whoami())

print(ela.policz_litery("abcdefg"))
podryw = ela.podrywaj(michal)
print(f"Podryw: {podryw}")
if podryw:
    print(f"Ela w Michale: {ela.zakochaj_sie(michal)}")
    print(f"Michał w Eli: {michal.zakochaj_sie(ela)}")
ela.wniosek(michal)