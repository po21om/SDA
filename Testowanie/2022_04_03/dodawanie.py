import operator
import pytest

def dej_number(a):
    return a


def dodawanie(y, x):
    return operator.add(dej_number(y), dej_number(x))



wynik = dodawanie("2","3")
if wynik == 5:
    print("Test dodawania ok")
else:
    print("Dodawanie nie działą")

def test_dodawanie_liczb_doodatnich():
    wynik = dodawanie ("2","3")
    assert wynik == "23"

def test_dodawanie_liczb_ujemnych():
    wynik = dodawanie ("2","-2")
    assert wynik == 0
