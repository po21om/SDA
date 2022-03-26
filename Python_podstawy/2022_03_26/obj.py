class Osoba:
    name = ""
    age = 0
    occupation = ""

    def __init__(self, name, age, occupation):
        self.__name = name
        self.age = age
        self.occupation = occupation

        # self.name = name # dostępne z zewnątrz
        # self._name = name # nadal dostępne z zewnatrz ale sugeruje by tego nie robic
        # self.__name = name # brak mozliwosci dostepu z zewnatrz, nadal mozna metoda wewnetrzna


    def whoami(self):
        print(f"Cześć, mam na imię {self.__name}, mam {self.age} lat i pracuję jako {self.occupation}.")

tomek = Osoba(name='Tomek', age=30, occupation='spawacz')
tomek.whoami()
eliza = Osoba(name='Eliza', age=27, occupation='sekretarka')
eliza.whoami()