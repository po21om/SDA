from typing import Union


class Vehicle:
    def get_brand(self) -> str:
        pass

    def get_wheels_count(self) -> int:
        pass

    def get_seats_count(self) -> int:
        pass

    def get_vehicle_type(self) -> str:
        """
        Any of air, land, water
        :return:
        """
        pass

    def get_engine_type(self) -> str:
        """
        Any of petrol, diesel, gas, electric
        :return:
        """
        pass


class Car(Vehicle):
    def __init__(self, brand: str, engine_type: str, wheels_count: int = 4, seats_count: int = 5,
                 vehicle_type: str = 'land'):
        self._brand = brand
        self._engine_type = engine_type
        self._wheels_count = wheels_count
        self._seats_count = seats_count
        self._vehicle_type = vehicle_type

    def get_brand(self) -> str:
        return self._brand

    def get_engine_type(self) -> str:
        return self._engine_type

    def get_seats_count(self) -> int:
        return self._seats_count

    def get_wheels_count(self) -> int:
        return self._wheels_count

    def get_vehicle_type(self) -> str:
        return self._vehicle_type

    def __str__(self):
        return f'Car: {self._brand} with {self._engine_type} engine.'


class Bike(Vehicle):
    def __init__(self, brand: str, engine_type: str = None, wheels_count: int = 2, seats_count: int = 1,
                 vehicle_type: str = 'land'):
        self._brand = brand
        self._engine_type = engine_type
        self._wheels_count = wheels_count
        self._seats_count = seats_count
        self._vehicle_type = vehicle_type

    def get_brand(self) -> str:
        return self._brand

    def get_engine_type(self) -> str:
        return self._engine_type

    def get_seats_count(self) -> int:
        return self._seats_count

    def get_wheels_count(self) -> int:
        return self._wheels_count

    def get_vehicle_type(self) -> str:
        return self._vehicle_type

    def __str__(self):
        return f'Bike: {self._brand} with {self._engine_type} engine.'


class Skateboard(Vehicle):
    def __init__(self, brand: str, wheels_count: int = 4,
                 vehicle_type: str = 'land'):
        self._brand = brand
        self._wheels_count = wheels_count
        self._vehicle_type = vehicle_type

    def get_brand(self) -> str:
        return self._brand

    def get_wheels_count(self) -> int:
        return self._wheels_count

    def get_vehicle_type(self) -> str:
        return self._vehicle_type

    def __str__(self):
        return f'Skateboard: {self._brand} with applied griptape.'


class Airplane(Vehicle):
    def __init__(self, brand: str, engine_type: str,  seats_count: int, wheels_count: int = 10,
                 vehicle_type: str = 'air'):
        self._brand = brand
        self._engine_type = engine_type
        self._wheels_count = wheels_count
        self._seats_count = seats_count
        self._vehicle_type = vehicle_type

    def get_brand(self) -> str:
        return self._brand

    def get_engine_type(self) -> str:
        return self._engine_type

    def get_seats_count(self) -> int:
        return self._seats_count

    def get_wheels_count(self) -> int:
        return self._wheels_count

    def get_vehicle_type(self) -> str:
        return self._vehicle_type

    def __str__(self):
        return f'Airplane: {self._brand} with {self._engine_type} engine and {self._seats_count} seats.'


class VehicleFactory:
    def create(self) -> Vehicle:
        pass


class BMWCarFactory(VehicleFactory):
    def create(self) -> Car:
        return Car('BMW', 'petrol')


class RometBikeFactory(VehicleFactory):
    def create(self) -> Bike:
        return Bike('Romet')


class ElementSkateboardFactory(VehicleFactory):
    def create(self) -> Skateboard:
        return Skateboard('Element')


class BoeingAirplaneFactory(VehicleFactory):
    def create(self) -> Airplane:
        return Airplane('Boeing', 'petrol', 168)


if __name__ == "__main__":
    vehicle_type = input('select vehicle type [bike, car, skateboard, airplane]: ')
    vehicle_factory: Union[VehicleFactory, None] = None
    if vehicle_type.lower() == 'bike':
        vehicle_factory = RometBikeFactory()
    elif vehicle_type.lower() == 'car':
        vehicle_factory = BMWCarFactory()
    elif vehicle_type.lower() == 'skateboard':
        vehicle_factory = ElementSkateboardFactory()
    elif vehicle_type.lower() == 'airplane':
        vehicle_factory = BoeingAirplaneFactory()
    if vehicle_factory:
        vehicle = vehicle_factory.create()
        print(vehicle)
    else:
        print('Not implemented')
