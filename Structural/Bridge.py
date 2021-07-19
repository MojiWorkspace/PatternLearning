# This program is based on Bridge pattern

# Situation: remotes used to control specific devices
# remote (Controller) for common Tv (Device)
# and another remote (ExplodeController) for exploding Tv (ExplodingTv)
# with using Bridge pattern idea

import os
import platform
from abc import ABC, abstractmethod


class Device(ABC):
    @abstractmethod
    def __init__(self):
        self.power = False
        self.volume = 0
        self.channel = 1


class Controller:
    def __init__(self, device: Device):
        self.device = device

    def toggle_power(self):
        if self.device.power is False:
            self.device.power = True
            print('\nDevice is now turned on\n')
        else:
            self.device.power = False
            print('\nDevice is now turned off\n')

    def volume_up(self, value):
        try:
            if self.device.power is False:
                print(f'\nCan\'t increase the volume by {value}\nDevice is turned off\n')
            else:
                if 10 < value < 0:
                    print(f'\nCan\'t increase the volume by {value}\nIncorrect value\n')
                    return
                else:
                    self.device.volume += value
                    print(f'\nVolume increased by {value}\n')
        except AttributeError:
            print('\nThis device doesn\'t have volume settings\n')

    def volume_down(self, value):
        try:
            if self.device.power is False:
                print(f'\nCan\'t reduce the volume by {value}\nDevice is turned off\n')
            else:
                if 10 < value < 0:
                    print(f'\nCan\'t reduce the volume by {value}\nIncorrect value\n')
                    return
                else:
                    self.device.volume -= value
                    print(f'\nVolume reduced by {value}\n')
        except AttributeError:
            print('\nThis device doesn\'t have volume settings\n')

    def switch_channel(self, value):
        try:
            if self.device.power is False:
                print(f'\nCan\'t switch by {value} channel\nDevice is turned off\n')
            else:
                if 30 < value < 1:
                    print(f'\nCan\'t switch by {value} channel\nIncorrect value\n')
                    return
                else:
                    self.device.channel = value
                    print(f'\nChannel switched by {value} channel\n')
        except AttributeError:
            print('\nThis device doesn\'t have channel settings\n')


class ExplodeController(Controller):
    def toggle_power(self):
        if self.device.power is False:
            print('\n###############\n'
                  '# BOOOOOOOOOM #\n'
                  '###############\n')
            self.device.power = True
        else:
            print('\nDevise has been destroyed\n')


class CommonTv(Device):
    def __init__(self):
        self.power = False
        self.volume = 0
        self.channel = 1


class ExplodingTv(Device):
    def __init__(self):
        self.power = False


def clear_cmd():
    if platform.system() == 'Linux':
        os.system('clear')
    elif platform.system() == 'Windows':
        os.system('cls')


def print_menu():
    clear_cmd()
    print('<1> Increase volume\n'
          '<2> Reduce volume\n'
          '<3> Change channel\n'
          '<4> Toggle power\n'
          '<0> Exit (Next stage)\n')


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


def client_code(abstraction: Controller):
    items = [1, 2, 3, 4, 0]
    print_menu()
    chosen_operation = int(-1)
    while chosen_operation != 0:
        chosen_operation = select_menu_item(items)
        if chosen_operation == 1:
            abstraction.volume_up(10)
            input('\nPress <Enter> to continue...')
            print_menu()
        elif chosen_operation == 2:
            abstraction.volume_down(10)
            input('\nPress <Enter> to continue...')
            print_menu()
        elif chosen_operation == 3:
            abstraction.switch_channel(1)
            input('\nPress <Enter> to continue...')
            print_menu()
        elif chosen_operation == 4:
            abstraction.toggle_power()
            input('\nPress <Enter> to continue...')
            print_menu()
        elif chosen_operation == 0:
            break


if __name__ == "__main__":
    # Device and controller initialization
    tv = CommonTv()
    controller = Controller(tv)

    client_code(controller)

    print("\n")

    # Device and controller initialization
    explosion_tv = ExplodingTv()
    explode_controller = ExplodeController(explosion_tv)

    client_code(explode_controller)
