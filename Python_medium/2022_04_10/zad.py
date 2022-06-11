# 1.Przygotować klasę do przechowywania informacji o kontach (imię i nazwisko, numer konta, saldo), na podstawie tej klasy utworzyć klasy pochodne opisujące konto firmowe i konto prywatne, konto firmowe powinno mieć dodatkowe metody do płacenia należności (np. ZUS i PIT - płacenie polega na wyświetleniu pełnej informacji). Ponadto obydwie klasy mają metodę wyświetlającą informację o koncie.
# a.Utworzyć przynajmniej po trzy nazwane obiekty każdej klasy.
# b.obiekty przechowujące konta firmowe zapisać na liście, wywołać obydwie metody (płacenia należności) z listy.
# c.dołożyć metody do zapisu i odczytu z pliku stanu kont i ich numerów (można stosować sposób - jeden plik jeden obiekt) - zapisać obiekty do pliku
# d.OP. Dołożyć classmethody do tworzenia konta za pomocą stringa
# 2.  Do poprzedniego zadania dopisać klasę użwyając dataclass przechowujące informacje o należnościach (wysokość kwoty i nr konta na który należy wpłacać). Następnie użyć tych informacji w metodach wypisujących dane o płatnościach.
# 3.  Przygotować klasę z metodą statyczną umożliwiającą wyknonywanie przelewów powiędzy kontami
# 4.  Zmienić dataclass należność i klasę wykonującą przelewy tak żeby klasa wykonująca przelewy mogła korzystać tylko z instancji klasy Należność

from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Bank(ABC):
    account_no: int
    balance: float



class Account(ABC):
    def __init__(self, fname: str, lname: str, account_no: int, balance: float):
        self.fname = fname
        self.lname = lname
        self.account_no = account_no
        self.balance = balance

    def __str__(self):
        return f'{self.fname} {self.lname} {self.account_no} {self.balance}'

    def save_account(self):
        with open(f'{self.fname}{self.lname}.txt', 'w') as file:
            file.write(f'{self.account_no} {self.balance}')

    def check_account(self):
        with open(f'{self.fname}{self.lname}.txt', 'r') as file:
            print(file.read())

    @classmethod
    def create_account(cls, text: str):
        fname, lname, account_no, balance = text.split()
        account_no, balance = int(account_no), float(balance)
        return cls(fname, lname, account_no, balance)

class CompanyAccount(Account):
    def __init__(self, fname: str, lname: str, account_no: int, balance: float):
        super().__init__(fname, lname, account_no, balance)

    def payPIT(self, how_much:float):
        self.balance -= how_much
        return f'{self.fname} {self.lname} {self.account_no} payed {how_much} to PIT'

    def payZUS(self, how_much:float):
        self.balance -= how_much
        return f'{self.fname} {self.lname} {self.account_no} payed {how_much} to ZUS'


class PersonalAccount(Account):
    def __init__(self, fname: str, lname: str, account_no: int, balance: float):
        super().__init__(fname, lname, account_no, balance)


comp_a = CompanyAccount("Jan", "Kowalski", 1234567890, 1000.00)
comp_b = CompanyAccount("Janusz", "Nowak", 3763733660, 2000.00)
comp_c = CompanyAccount("Ilona", "Duszyńska", 9987654321, 3000.00)

pers_a = PersonalAccount("Marek", "Jurek", 123525665, 550.00)
pers_b = PersonalAccount("Jurek", "Fasola", 838356835, 784.00)
pers_c = PersonalAccount("Alina", "Onufry", 1835835683, 990.00)


comp_list = [comp_a, comp_b, comp_c]
for comp in comp_list:
    print(comp.payPIT(100.00))
    print(comp.payZUS(500.00))

comp_z = CompanyAccount.create_account('John Wayne 1241515 1234.00')
pers_z = PersonalAccount.create_account('Mia Mikowski 876443637 23546.80')

comp_z.save_account()
comp_z.check_account()