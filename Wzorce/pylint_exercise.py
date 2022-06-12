"""Sample Garden module"""
from typing import List, Union


class Garden:
    """Sample Garden class"""
    def __init__(self, area: Union[float, None] = None):
        self._plants = []
        self._area = area

    def get_garden_area(self) -> Union[float, None]:
        """
        Returns garden area.

        :return: garden area
        """
        return self._area

    def get_all_plants(self) -> List[str]:
        """
        Returns list of all plants in the garden.

        :return plants: List of plants
        """
        return self._plants

    def add_plant(self, plant: str) -> None:
        """
        Appends given plant to the garden plants list.

        :param plant: plant name
        :return None:
        """
        self._plants.append(plant)


if __name__ == '__main__':
    garden = Garden(10.3)
    print(garden.get_garden_area())
    garden.add_plant("Sunflower")
    print(garden.get_all_plants())
