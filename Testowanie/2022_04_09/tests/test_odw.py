import pytest
from odw import OdwrotnieClass

#def test_funkcja():
#    assert False

def test_create():
    rev = OdwrotnieClass(name="abcdef")
    assert rev._name == "abcdef"


def test_reverse():
    rev = OdwrotnieClass(name="abcdef")
    assert rev.reverse() == "fedcba"


def test_reverse_two():
    rev = OdwrotnieClass(name="abcdef")
    wynik = rev.reverse()
    assert  wynik == "fedcba"


def test_empty():
    rev = OdwrotnieClass(name="")
    wynik = rev.reverse()
    #assert wynik == ""
    assert not wynik
    assert isinstance(wynik, str)


def test_int():
    rev = OdwrotnieClass(name=345)
    wynik = rev.reverse()
    assert wynik == "543"
