import pytest
from calculator import Calc


def test_calc_class_create():
    cal = Calc(a=2, b=4)
    assert cal.a == 2 and cal.b == 4

def test_add_positive_numbers():
    cal = Calc(a=2, b=4)
    assert cal.add() == 6

def test_add_negative_numbers():
    cal = Calc(a=-3, b= -7)
    assert cal.add() == -10

def test_sub_positive_numbers():
    cal = Calc(a=2, b=4)
    assert cal.sub() == -2

def test_sub_negative_numbers():
    cal = Calc(a=-3, b= -7)
    assert cal.sub() == 4

def test_sub_positive_numbers_reversed():
    cal = Calc(a=2, b=4)
    assert cal.sub(reverse=True) == 2

def test_sub_negative_numbers_reversed():
    cal = Calc(a=-3, b= -7)
    assert cal.sub(reverse=True) == -4

def test_mul_positive_numbers():
    cal = Calc(a=2, b=4)
    assert cal.mul() == 8

def test_mul_negative_numbers():
    cal = Calc(a=-3, b= -7)
    assert cal.mul() == 21

def test_mul_by_zero():
    cal = Calc(a=3, b=0)
    assert cal.mul() == 0

def test_div_positive_numbers():
    cal = Calc(a=2, b=4)
    assert cal.div() == 0.5

def test_div_negative_numbers():
    cal = Calc(a=-3, b= -12)
    assert cal.div() == 0.25

def test_div_positive_numbers_reversed():
    cal = Calc(a=2, b=4)
    assert cal.div(reverse=True) == 2

def test_div_negative_numbers_reversed():
    cal = Calc(a=-3, b= -12)
    assert cal.div(reverse=True) == 4

def test_div_by_zero():
    cal = Calc(a=8, b=0)
    with pytest.raises(ZeroDivisionError):
        assert cal.div()