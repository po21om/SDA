import operator


def dej_number(a):
    return a


def dej_nurnber(a):
    return int(a)


def dodawanie(y, x):
    return operator.add(dej_number(y), dej_number(x))


def odejmowanie(y, x):
    return operator.sub(dej_nurnber(x), dej_nurnber(y))


def dzielenie(y, x):
    return operator.div(dej_nurnber(y), dej_nurnber(x))


def mnozenie(y, x):
    return operator.mul(dej_nurnber(y), dej_number(x))


def main():
    w = 0
    x = input("podaj pierwsza liczbe: ")
    z = input("podaj znak dzialania: ")
    y = input("podaj druga liczbe: ")

    if z == "+":
        w = dodawanie(x, y)
    elif z == "-":
        w = odejmowanie(x, y)
    elif z == "*":
        w = mnozenie(x, y)
    elif z == "/":
        w = dzielenie(y, x)

    print(w)


if __name__ == '__main__':
    main()