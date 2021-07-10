# This program is based on Builder pattern.
# Script represents house-building process
# Each house consist of parts: roof, walls, door, windows
# Client (user) can build a house step by step choosing the material of each part
# (Which builder will make chosen part)

from abc import ABC, abstractmethod
import os
import sys
import platform
import datetime


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
        # self.reset()
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
        # self.reset()
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
        # self.reset()
        return house

    def make_roof(self):
        self._house.add("Part: Jelly Roof")

    def make_walls(self):
        self._house.add("Part: Jelly Walls")

    def make_door(self):
        self._house.add("Part: Jelly Door")

    def make_windows(self):
        self._house.add("Part: Jelly Windows")


class House:
    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

    def list_parts(self):
        clear_cmd()
        print(f'The house is built from the following parts:')
        for part in range(len(self.parts)):
            print(self.parts[part])
        print(f'\nBuilding complete: {current_datetime()}')


def current_datetime():
    now = datetime.datetime.now()
    return now.strftime('%Y-%m-%d %H:%M:%S')


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


def client_ui(team: list):
    choose_roof(team)


def choose_roof(team: list):
    items = [1, 2, 3, 0]
    clear_cmd()
    print('Please choose the material of the roof\n'
          'Confirm your choice by <Enter>\n\n'
          '<1> Stone\n'
          '<2> Wood\n'
          '<3> Jelly\n'
          '<0> Exit\n')
    chosen_material = int(-1)
    while chosen_material < 0 or chosen_material > 3:
        chosen_material = select_menu_item(items)
        if chosen_material == 1:
            team[0].make_roof()
            choose_walls(team)
        elif chosen_material == 2:
            team[1].make_roof()
            choose_walls(team)
        elif chosen_material == 3:
            team[2].make_roof()
            choose_walls(team)
        elif chosen_material == 0:
            clear_cmd()
            print('Program shutdown')
            sys.exit()


def choose_walls(team: list):
    items = [1, 2, 3, 0]
    clear_cmd()
    print('Please choose the material of the walls\n'
          'Confirm your choice by <Enter>\n\n'
          '<1> Stone\n'
          '<2> Wood\n'
          '<3> Jelly\n'
          '<0> Exit\n')
    chosen_material = int(-1)
    while chosen_material < 0 or chosen_material > 3:
        chosen_material = select_menu_item(items)
        if chosen_material == 1:
            team[0].make_walls()
            choose_door(team)
        elif chosen_material == 2:
            team[1].make_walls()
            choose_door(team)
        elif chosen_material == 3:
            team[2].make_walls()
            choose_door(team)
        elif chosen_material == 0:
            clear_cmd()
            print('Program shutdown')
            sys.exit()


def choose_door(team: list):
    items = [1, 2, 3, 0]
    clear_cmd()
    print('Please choose the material of the door\n'
          'Confirm your choice by <Enter>\n\n'
          '<1> Stone\n'
          '<2> Wood\n'
          '<3> Jelly\n'
          '<0> Exit\n')
    chosen_material = int(-1)
    while chosen_material < 0 or chosen_material > 3:
        chosen_material = select_menu_item(items)
        if chosen_material == 1:
            team[0].make_door()
            choose_windows(team)
        elif chosen_material == 2:
            team[1].make_door()
            choose_windows(team)
        elif chosen_material == 3:
            team[2].make_door()
            choose_windows(team)
        elif chosen_material == 0:
            clear_cmd()
            print('Program shutdown')
            sys.exit()


def choose_windows(team: list):
    items = [1, 2, 3, 0]
    clear_cmd()
    print('Please choose the material of the windows\n'
          'Confirm your choice by <Enter>\n\n'
          '<1> Stone\n'
          '<2> Wood\n'
          '<3> Jelly\n'
          '<0> Exit\n')
    chosen_material = int(-1)
    while chosen_material < 0 or chosen_material > 3:
        chosen_material = select_menu_item(items)
        if chosen_material == 1:
            team[0].make_windows()
        elif chosen_material == 2:
            team[1].make_windows()
        elif chosen_material == 3:
            team[2].make_windows()
        elif chosen_material == 0:
            clear_cmd()
            print('Program shutdown')
            sys.exit()


if __name__ == "__main__":
    # House initialization
    house = House()

    # Builders initialization
    builder_stone = StoneBuilder()
    builder_wood = WoodenBuilder()
    builder_jelly = JellyBuilder()

    # Bring builders in team
    builders = [builder_stone, builder_wood, builder_jelly]

    # UI
    client_ui(builders)

    # Build the house
    for builder in range(len(builders)):
        house.parts = house.parts + builders[builder].house.parts

    # Show the building result
    house.list_parts()