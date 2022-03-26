# dobra praktyka - by każda class-a była w osobnym pliku
import datetime
import uuid
from random import randint, random, choice



class Osoba:
    def __init__(self, name=None, sex=None):
        self.name = name
        self.sex = sex # 0 - M, 1 - K
        self.__age = randint(1, 120) # Losowa warotść (1-120)

    @property
    def age(self):
        return self.__age

    def whoami(self):
        return [self.name, self.sex, self.__age]

    def policz_litery(self, text):
        return len(text)

    def przywitaj_sie(self, osoba):
        print(f"Cześć, {osoba.name}!")

    def podrywaj(self,osoba):
        age_diff = abs(self.__age - osoba.age)
        if age_diff > 40:
            return False
        elif age_diff > 20:
            return True if random() < 0.2 else False
        elif age_diff > 10:
            return True if  choice([True, False, False]) < 0.33 else False
        else:
            return True if randint(0,1) < 0.5 else False

    def zakochaj_sie(self, osoba):
        len_of_names = len(self.name)+len(osoba.name)
        if len_of_names < 7:
            return True
        elif len_of_names > 20:
            if len(self.name) >= len(osoba.name):
                return True
            else:
                return False
        else:
            if "a" in self.name.lower() and "a" in osoba.name.lower():
                return True if random() < 0.8 else False
            elif "i" in self.name.lower() or "i" in osoba.name.lower():
                return True if random() < 0.7 else False
            else:
                return False

    def wniosek(self, osoba):
        with open(f"wniosek_{str(datetime.date.today())}_{uuid.uuid4()}.txt", "w", encoding="UTF-8") as f:
            f.write(f"{self.name}, {self.sex}, {self.__age} - {osoba.name}, {osoba.sex}, {osoba.age}")