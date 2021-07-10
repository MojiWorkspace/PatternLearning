# This program is based on Builder pattern (check Builder.py) with Director
# Director gives an opportunity to produce objects with predefined configurations
# (and predefined sequence)
# Director class is not necessary, because client can lead builders
# This script provided without UI


from abc import ABC, abstractmethod
import os
import platform


class Builder(ABC):

    @property
    @abstractmethod
    def house(self):
        pass

    @abstractmethod
    def make_roof(self):
        pass

    @abstractmethod
    def make_walls(self):
        pass

    @abstractmethod
    def make_door(self):
        pass

    @abstractmethod
    def make_windows(self):
        pass


class StoneBuilder(Builder):

    def __init__(self):
        self.reset()

    def reset(self):
        self._house = House()

    @property
    def house(self):
        house = self._house
        self.reset()
        return house

    def make_roof(self):
        self._house.add("Part: Stone Roof")

    def make_walls(self):
        self._house.add("Part: Stone Walls")

    def make_door(self):
        self._house.add("Part: Stone Door")

    def make_windows(self):
        self._house.add("Part: Stone Windows")


class WoodenBuilder(Builder):

    def __init__(self):
        self.reset()

    def reset(self):
        self._house = House()

    @property
    def house(self):
        house = self._house
        self.reset()
        return house

    def make_roof(self):
        self._house.add("Part: Wooden Roof")

    def make_walls(self):
        self._house.add("Part: Wooden Walls")

    def make_door(self):
        self._house.add("Part: Wooden Door")

    def make_windows(self):
        self._house.add("Part: Wooden Windows")


class JellyBuilder(Builder):

    def __init__(self):
        self.reset()

    def reset(self):
        self._house = House()

    @property
    def house(self):
        house = self._house
        self.reset()
        return house

    def make_roof(self):
        self._house.add("Part: Jelly Roof")

    def make_walls(self):
        self._house.add("Part: Jelly Walls")

    def make_door(self):
        self._house.add("Part: Jelly Door")

    def make_windows(self):
        self._house.add("Part: Jelly Windows")


class Director:

    def __init__(self):
        self._builder = None

    @property
    def builder(self):
        return self._builder

    @builder.setter
    def builder(self, builder: Builder):
        self._builder = builder

    def build_full_house(self):
        self.builder.make_roof()
        self.builder.make_walls()
        self.builder.make_door()
        self.builder.make_windows()

    def build_walls_and_door(self):
        self.builder.make_walls()
        self.builder.make_door()

    def build_windows_and_roof(self):
        self.builder.make_windows()
        self.builder.make_roof()


class House:
    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

    def list_parts(self):
        print(f'Produced parts:')
        for part in range(len(self.parts)):
            print(self.parts[part])
        print('\n')


def clear_cmd():
    if platform.system() == 'Linux':
        os.system('clear')
    elif platform.system() == 'Windows':
        os.system('cls')


# Menu items choosing function
def select_menu_item(itemlist: list):
    item = int(-1)
    while item not in itemlist:
        try:
            item = int(input('Enter your choice: '))
            if item < min(itemlist) or item > max(itemlist):
                print(f'\nOperation \"{item}\" is not available\n')
        except ValueError:
            print('\nInput value error\nNot an integer\n\nPlease repeat the input\n\n')
    return item


if __name__ == "__main__":
    clear_cmd()

    # House initialization for custom house (made by group of builders)
    house = House()

    # Builders initialization
    builder_stone = StoneBuilder()
    builder_wood = WoodenBuilder()
    builder_jelly = JellyBuilder()

    # Director initialization
    director = Director()

    print('##############################')
    print('Producing with Director\n')
    # Building full-wooden house using Director
    director.builder = builder_wood
    director.build_full_house()
    builder_wood.house.list_parts()

    # All kind of available producing configurations with Director
    # (Each director's function creates new object wih another configuration)

    # Walls and Door
    director.builder = builder_jelly
    director.build_walls_and_door()
    builder_jelly.house.list_parts()
    # Full Jelly House
    director.build_full_house()
    builder_jelly.house.list_parts()
    # Windows and Roof
    director.build_windows_and_roof()
    builder_jelly.house.list_parts()

    # Stone windows and Roof
    director.builder = builder_stone
    director.build_windows_and_roof()
    builder_stone.house.list_parts()
    print('##############################n\n\n')

    # Custom configuration
    print('##############################')
    print('Client\'s custom configuration\n')
    builder_jelly.make_walls()
    builder_wood.make_door()
    builder_wood.make_roof()
    builder_stone.make_walls()
    # We can see what each of builders has done
    builder_jelly.house.list_parts()
    builder_wood.house.list_parts()
    builder_stone.house.list_parts()
    # or like this
    print('Client\'s custom configuration\n')
    builder_jelly.make_walls()
    builder_wood.make_door()
    builder_wood.make_roof()
    builder_stone.make_walls()
    house.parts = builder_jelly.house.parts + builder_wood.house.parts + builder_stone.house.parts
    house.list_parts()
    print('##############################')