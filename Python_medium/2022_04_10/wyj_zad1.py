#Napisz interaktywny kalkulator który na wejściu pobierze od użytkownika formułę (liczba, spacja, operator(+,-,*,/), spacja, liczba). A następnie:
#1. Jeżeli formuła wprowadzona przez użytkownika nie spełnia założonego schematu (liczba, spacja, operator(+,-,*,/), spacja, liczba). Rzuć własnoręcznie stworzonym wyjątkiem FormulaError.
#2. Jeżeli został rzucony ValueError. Wypisz na ekranie której liczby dotyczył
#3. Spróbuj przewidzieć inne wyjątki które mogą wystąpić i jeśli wystąpią wypisz własny komunikat
#4. Jeżeli wszystko jest ok. Oblicz, wypisz wynik na ekran oraz zapętl program

class CalcException(Exception):
    def __init__(self):
        message = "Działanie nie jest w formacie liczba-spacja-operator-spacja-liczba"
        super().__init__(message)


def calculator():
    while True:
        string = input("Wprowadź działanie: ")
        if string == "exit"
            break
        if len(string) < 5:
            raise CalcException()


        num_1 = string[:string.find(" ")]
        operator = string[string.find(" ") + 1:string.find(" ") + 2]
        num_2 = string[string.find(" ", string.find(" ") + 1) + 1:]


        try:
            num_1 = float(num_1)
        except ValueError:
            print (f"'{num_1}' nie jest liczbą")
            continue


        try:
            num_2 = float(num_2)
        except ValueError:
            print (f"'{num_2}' nie jest liczbą")
            continue


        if operator == "+":
            print(f'{num_1 + num_2}')
        elif operator == "-":
            print(f'{num_1 - num_2}')
        elif operator == "*":
            print(f'{num_1 * num_2}')
        elif operator == "/":
            try:
                print(f'{num_1 / num_2}')
            except ZeroDivisionError:
                print("Nie dzielimy przez 0.")

        else:
            print(f'"{operator}" to nie jest wspierany operator')


calculator()