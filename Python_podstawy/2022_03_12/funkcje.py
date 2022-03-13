owoce = ["Ananas", "Banan", "Kiwi", "Arbuz"]
def middle_letter(str):
    return str[int((len(str)-1)/2):int((len(str)+2)/2)]

print([middle_letter(owoc) for owoc in owoce])
# print(middle_letter(owoce[1]))
# print(middle_letter(owoce[2]))
# print(middle_letter(owoce[3]))

def kwadrat(number):
    return number**2


def nia_check(string) -> bool:
    return True if "nia" in string else False

print(nia_check("olek"))

def powitaj(name="nieznajomy"):
    return(f"Witamy {name}!")
print(powitaj())
print(powitaj("Piotrek"))


def add(*args): # trafiaja do tupli
    return sum(args)
print(add(1, 2, 3, 4, 5, 6))


def wypisz(*args):
    for arg in args:
        print(arg)

wypisz("Janek", "Tomek", "Luiza")

# Stwórz menu
# czasy oczekiwania args
# nazwy potraw i ceny kwargs
def menu(*czasy,**potrawy):
    #print(czasy)
    # for czas in czasy:
    #     print(czas)
    #print(potrawy)
    val_list = [potrawa for potrawa in potrawy]

    for potrawa in potrawy:
        index = list(potrawy.keys()).index(potrawa)
        print(f"{potrawa} - {potrawy[potrawa]} zł - {czasy[index]} min")

menu(15, 20, 30, 50, jajecznica = 12, żurek = 18)
