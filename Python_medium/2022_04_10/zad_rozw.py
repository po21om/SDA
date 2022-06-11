from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class Naleznosc:
    kwota_do_zaplaty: int
    nr_konta: str



class Konto(ABC):
    def __init__(self, imie, nazwisko, numer_konta, saldo):
        self.imie = imie
        self.nazwisko = nazwisko
        self.numer_konta = numer_konta
        self.saldo = saldo

    @abstractmethod
    def print_info(self):
        pass

    @abstractmethod
    def save_account_state_to_file(self):
        pass

    @abstractmethod
    def load_account_state_from_file(self):
        pass

class KontoPrywatne(Konto):
    def print_info(self):
        print(f'Imie: {self.imie}\nNazwisko: {self.nazwisko}\nNumer konta: {self.numer_konta}\nSaldo: {self.saldo}')

    def save_account_state_to_file(self):
        with open(f'{self.numer_konta}.txt', 'w') as file:
            file.write(f'{self.numer_konta} {self.saldo}')

    def load_account_state_from_file(self):
        pass


class KontoFirmowe(Konto):
    def __init__(self, imie, nazwisko, numer_konta, saldo, naleznosc_zus, naleznosc_pit):
        super().__init__(imie, nazwisko, numer_konta, saldo)
        self.naleznosc_zus = naleznosc_zus
        self.naleznosc_pit = naleznosc_pit

    def print_info(self):
        print(f'KONTO FIRMOWE\nImie: {self.imie}\nNazwisko: {self.nazwisko}\nNumer konta: {self.numer_konta}\nSaldo: {self.saldo}')

    def zaplac_pit(self):
        print(f"Płacę PIT w wysokości {self.naleznosc_pit.kwota_do_zaplaty}")

    def zaplac_zus(self):
        print(f"Płacę ZUS w wysokości {self.naleznosc_zus.kwota_do_zaplaty}")

    def save_account_state_to_file(self):
        with open(f'{self.numer_konta}.txt', 'w') as file:
            file.write(f'{self.numer_konta} {self.saldo}')

    def load_account_state_from_file(self):
        pass

class PrzelewMaker:
    @staticmethod
    def make_przelew(kwota, z_konta, na_konto):
        if z_konta.saldo >= kwota:
            z_konta.saldo -= kwota
            na_konto.saldo += kwota
        else:
            print("\nNie wykonano przelewu.\nZa mało środków na koncie.\n")

kp1 = KontoPrywatne("Witold", "Bazela", "97863425412", 0)
kp2 = KontoPrywatne("Urszula", "Bazela", "43632673737", 1000)
kp3 = KontoPrywatne("Paulina", "Bazela", "38275654747", 800)
kp1.print_info()
nal1_zus = Naleznosc(100, "100000")
nal1_pit = Naleznosc(200, "1245124")
kf1 = KontoFirmowe("Johnny", "Mnemonic", "1241565", 10000,nal1_zus, nal1_pit)

#kf2 = KontoFirmowe("Marc", "Mnemonic", "636262", 18000)
#kf3 = KontoFirmowe("Ada", "Mnemonic", "2637484", 80000)
kf1.print_info()
kfs = [kf1]#, kf2, kf3]
for kf in kfs:
    kf.zaplac_pit()
    kf.zaplac_zus()
#kp1.save_account_state_to_file()

PrzelewMaker.make_przelew(100, kp1, kp3)
kp1.print_info()
kp3.print_info()