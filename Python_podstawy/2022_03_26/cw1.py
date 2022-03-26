class Osoba:
    def __init__(self, imie=None, plec=None, wiek=None, stanCyw=None, stanKonta=None):
        self.imie = imie
        self.plec = plec
        self.wiek = wiek
        self.__stanCyw = stanCyw
        self.__stanKonta = stanKonta

    @property
    def stanKonta(self):
        return self.__stanKonta

    @stanKonta.setter
    def stanKonta(self, num=0):
        if num >= 0:
            self.__stanKonta = num
        else:
            print("Konto nie może posiadać debetu")

    @stanKonta.deleter
    def stanKonta(self):
        del self.__stanKonta


ela = Osoba(imie="Ela", plec="K", wiek=28, stanCyw="panna", stanKonta=10000)
print(ela.stanKonta)
ela.stanKonta = 12345
print(ela.stanKonta)
ela.stanKonta = -200