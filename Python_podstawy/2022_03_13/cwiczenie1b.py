import random as r

names= ["Adam","Zbigniew", "Pankracy", "Jolanta", "Genowefa", 'Zofia']
def Osoba( 😞    return [("Imie",names[r.randint(0,5)]),("Wiek",r.randint(17,70)),("Stan konta",r.randint(300, 450000))]

postac=Osoba()
postac.append(("praca",r.randint(0,1)))
postac.append(("ślub",r.randint(0,1)))
print(postac)