import operator

def dej_number(a):
    return a


def dej_nurnber(a):
    return int(a)


def mnozenie(y, x):
    return operator.mul(dej_nurnber(y), dej_number(x))


def test_mnozenie_liczb_dodatnich():
    wynik = mnozenie("8", "8")
    assert wynik == 64

def test_mnozenie_liczb_pierwszej_ujemnej():
    wynik = mnozenie("-8", "8")
    assert wynik == -64

def test_mnozenie_liczb_drugiej_ujemnej():
    wynik = mnozenie("8", "-8")
    assert wynik == -64

def test_mnozenie_liczb_dwoch_ujemnych():
    wynik = mnozenie("-8", "-8")
    assert wynik == 64

def test_mnozenie_liczb_dwucyfrowych():
    wynik = mnozenie("12", "12")
    assert wynik == 144

def test_mnozenie_pierwszej_float():
    wynik = mnozenie("0.5", "10")
    assert wynik == 5

def test_mnozenie_drugiej_float():
    wynik = mnozenie("10", "0.5")
    assert wynik == 5

def test_mnozenie_dwoch_float():
    wynik = mnozenie("0.5", "0.5")
    assert wynik == 0.25