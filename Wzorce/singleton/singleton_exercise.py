from singleton_metaclass import SingletonMeta
from singleton_decorator import singleton


class Cake(metaclass=SingletonMeta):
    def __init__(self):
        self._name: str = ''

    def set_name(self, name: str):
        self._name = name

    def get_name(self) -> str:
        return self._name


@singleton
class Cake2:
    def __init__(self):
        self._name: str = ''

    def set_name(self, name: str):
        self._name = name

    def get_name(self) -> str:
        return self._name


if __name__ == '__main__':
    cake1 = Cake()
    cake1.set_name('Makowiec')
    cake2 = Cake()
    cake2.set_name('Szarlotka')
    if cake1.get_name() == cake2.get_name():
        print('I\'m a Singleton!')
    else:
        print('I\'m not a Singleton :(')

    cake3 = Cake2()
    cake3.set_name('Makowiec')
    cake4 = Cake2()
    cake4.set_name('Szarlotka')
    if cake1.get_name() == cake2.get_name():
        print('I\'m a Singleton!')
    else:
        print('I\'m not a Singleton :(')

