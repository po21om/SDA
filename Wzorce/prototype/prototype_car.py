import copy

from Wzorce.factory_method.factory_method_vehicle import Car


class Car:
    def __init__(self, wheels_count: int, doors_count: int, brand: str = '', model: str ='', color: str = ''):
        self._wheels_count = wheels_count
        self._doors_count = doors_count
        self._brand = brand
        self._color = color
        self._model = model

    @property # otwarcie pola do edycji
    def wheels_count(self) -> int:
        return self._wheels_count

    @wheels_count.setter
    def wheels_count(self, value: int) -> None:
        self._wheels_count = value

    # def get_wheels_count(self) -> int:
    #     return self._wheels_count
    #
    # def set_wheels_count(self, value) -> None:
    #     self._wheels_count = value

    @property
    def doors_count(self) -> int:
        return self._doors_count

    @doors_count.setter
    def doors_count(self, value: int) -> None:
        self._wheels_count = value

    @property
    def brand(self) -> str:
        return self._brand

    @brand.setter
    def brand(self, value: str) -> None:
        self._brand = value

    @property
    def color(self) -> str:
        return self._color

    @color.setter
    def color(self, value: str) -> None:
        self._color = value

    @property
    def model(self) -> str:
        return self._model

    @model.setter
    def model(self, value: str) -> None:
        self._model = value

    def clone(self) -> Car:
        return copy.copy(self)

    def __str__(self):
        return f'Car: {self._brand} in {self._color} color with ' \
               f'{self._wheels_count} wheels and {self._doors_count} doors.'


class CarManager:
    _base_car = Car(4, 5)

    @staticmethod
    def create_car_with_color(brand: str,  model: str, color: str) -> Car:
        base_car_clone = CarManager._base_car.clone()
        base_car_clone.brand = brand
        base_car_clone.model = model
        base_car_clone.color = color
        return base_car_clone


if __name__ == "__main__":
    car_1 = CarManager.create_car_with_color('Audi', 'A4', 'Pink')
    car_2 = CarManager.create_car_with_color('Skoda', 'Fabia', 'Aquamarine')

    print(car_1)
    print(car_2)