# This program is based on Builder pattern.
# Script represents house-building process
# Each house consist of parts: roof, walls, door, windows
# Client (user) can build a house step by step choosing the material of each part
# (Which builder will make chosen part)

from abc import ABC, abstractmethod
import os
import sys
import platform
import time
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
        print(f'The house is built from the following parts:')
        for part in range(len(self.parts)):
            print(self.parts[part])


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


def choose_roof():
    items = [1, 2, 3, 0]
    clear_cmd()
    print('Please choose the material of the roof\n'
          'Confirm your choice by <Enter>\n\n'
          '<1> Stone\n'
          '<2> Wood\n'
          '<3> Jelly\n'
          '<0> Exit\n')
    chosen_material = int(-1)
    while chosen_material != 0:
        chosen_material = select_menu_item(items)
        if chosen_material == 1:
            pass
        elif chosen_material == 2:
            pass
        elif chosen_material == 3:
            pass

    clear_cmd()
    print('Program shutdown')
    sys.exit()


def choose_walls():
    items = [1, 2, 3, 0]
    clear_cmd()
    print('Please choose the material of the walls\n'
          'Confirm your choice by <Enter>\n\n'
          '<1> Stone\n'
          '<2> Wood\n'
          '<3> Jelly\n'
          '<0> Back\n')
    chosen_material = int(-1)
    while chosen_material != 0:
        chosen_material = select_menu_item(items)
        if chosen_material == 1:
            pass
        elif chosen_material == 2:
            pass
        elif chosen_material == 3:
            pass

    choose_roof()


def choose_door():
    items = [1, 2, 3, 0]
    clear_cmd()
    print('Please choose the material of the door\n'
          'Confirm your choice by <Enter>\n\n'
          '<1> Stone\n'
          '<2> Wood\n'
          '<3> Jelly\n'
          '<0> Back\n')
    chosen_material = int(-1)
    while chosen_material != 0:
        chosen_material = select_menu_item(items)
        if chosen_material == 1:
            pass
        elif chosen_material == 2:
            pass
        elif chosen_material == 3:
            pass

    choose_walls()


def choose_windows():
    items = [1, 2, 3, 0]
    clear_cmd()
    print('Please choose the material of the windows\n'
          'Confirm your choice by <Enter>\n\n'
          '<1> Stone\n'
          '<2> Wood\n'
          '<3> Jelly\n'
          '<0> Back\n')
    chosen_material = int(-1)
    while chosen_material != 0:
        chosen_material = select_menu_item(items)
        if chosen_material == 1:
            pass
        elif chosen_material == 2:
            pass
        elif chosen_material == 3:
            pass

    choose_door()


if __name__ == "__main__":
    # Builders initialization
    builder_stone = StoneBuilder()
    builder_wood = WoodenBuilder()
    builder_jelly = JellyBuilder()

    print('Build your own house with STONE, WOOD and JELLY')

    # Each builder makes different parts for client house
    builder_wood.make_roof()
    builder_stone.make_walls()
    builder_jelly.make_door()
    builder_jelly.make_windows()

    # Build the house based on the configuration
    house = House()
    house.parts = builder_wood.house.parts + \
                  builder_stone.house.parts + \
                  builder_jelly.house.parts

    house.list_parts()