from osoba import Osoba

class Urzednik(Osoba):
    def __init__(self, name, sex, wydzial):
        super().__init__(name, sex)
        self.wydzial = wydzial

    def rozpatrz_wniosek(self):
        with open(f"wniosek_2022-03-26_38ff9516-051d-4402-8d67-5b37aee4a001.txt", "r", encoding="UTF-8") as f:
            wniosek = f.readline().split()
            print(wniosek)
            if int(wniosek[2]) >=18  and int(wniosek[6]) >=18:
                print("Przyznano")
                return True
            else:
                print("Nie przyznano")
                return False