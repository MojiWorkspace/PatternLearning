# This program is based on Abstract Factory pattern.
# Script represents the work of the factory
# that produces creatures from SAME MATERIAL parts
# Client (user) chooses the material from main menu and observe the shown process


from abc import ABC, abstractmethod
import os
import sys
import platform
import time
import datetime


# Abstract factory class that returns abstract objects
class AbstractFactory(ABC):

    @abstractmethod
    def create_head(self):
        pass

    @abstractmethod
    def create_body(self):
        pass

    @abstractmethod
    def create_legs(self):
        pass


class FleshFactory(AbstractFactory):

    def create_head(self):
        return FleshHead()

    def create_body(self):
        return FleshBody()

    def create_legs(self):
        return FleshLegs()


class CyberneticFactory(AbstractFactory):

    def create_head(self):
        return CyberneticHead()

    def create_body(self):
        return CyberneticBody()

    def create_legs(self):
        return CyberneticLegs()


class MagicFactory(AbstractFactory):

    def create_head(self):
        return MagicHead()

    def create_body(self):
        return MagicBody()

    def create_legs(self):
        return MagicLegs()


# Abstract head class
class AbstractHead(ABC):

    @abstractmethod
    def head_function(self):
        pass


class FleshHead(AbstractHead):

    def head_function(self):
        return 'Flesh Head'


class CyberneticHead(AbstractHead):

    def head_function(self):
        return 'Cybernetic Head'


class MagicHead(AbstractHead):

    def head_function(self):
        return 'Magic Head'


# Abstract body class
class AbstractBody(ABC):

    @abstractmethod
    def body_function(self):
        pass

    @abstractmethod
    def connection_info(self, collaborator: AbstractHead):
        pass


class FleshBody(AbstractBody):

    def body_function(self):
        return 'Flesh Body'

    def connection_info(self, collaborator: FleshHead):
        connect_to = collaborator.head_function()
        return f'Connecting {self.body_function()} to {connect_to}'


class CyberneticBody(AbstractBody):

    def body_function(self):
        return 'Cybernetic Body'

    def connection_info(self, collaborator: CyberneticHead):
        connect_to = collaborator.head_function()
        return f'Connecting {self.body_function()} to {connect_to}'


class MagicBody(AbstractBody):

    def body_function(self):
        return 'Magic Body'

    def connection_info(self, collaborator: MagicHead):
        connect_to = collaborator.head_function()
        return f'Connecting {self.body_function()} to {connect_to}'


# Abstract legs class
class AbstractLegs(ABC):

    @abstractmethod
    def legs_function(self):
        pass

    @abstractmethod
    def connection_info(self, collaborator: AbstractBody):
        pass


class FleshLegs(AbstractLegs):

    def legs_function(self):
        return 'Flesh Legs'

    def connection_info(self, collaborator: FleshBody):
        connect_to = collaborator.body_function()
        return f'Connecting {self.legs_function()} to {connect_to}'


class CyberneticLegs(AbstractLegs):

    def legs_function(self):
        return 'Cybernetic Legs'

    def connection_info(self, collaborator: CyberneticBody):
        connect_to = collaborator.body_function()
        return f'Connecting {self.legs_function()} to {connect_to}'


class MagicLegs(AbstractLegs):

    def legs_function(self):
        return 'Magic Legs'

    def connection_info(self, collaborator: MagicBody):
        connect_to = collaborator.body_function()
        return f'Connecting {self.legs_function()} to {connect_to}'


def client_operation(factory: AbstractFactory):
    head = factory.create_head()
    body = factory.create_body()
    legs = factory.create_legs()

    print('Producing...\n')
    time.sleep(1)
    print(f'{head.head_function()} (ready)\n')
    time.sleep(1)
    print(f'{body.body_function()} (ready)\n\n{body.connection_info(head)}...\n')
    time.sleep(2)
    print(f'{legs.legs_function()} (ready)\n\n{legs.connection_info(body)}...\n')
    time.sleep(2)
    print(f'{current_datetime()}\nProducing complete\n\nPress <Enter> to continue')
    input()


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


def print_menu():
    clear_cmd()
    print('#############\n# MAIN MENU #\n#############\n\n'
          'Please choose the material to produce the creature\n'
          'Confirm your choice by <Enter>\n\n'
          '<1> Flesh\n'
          '<2> Cybernetic\n'
          '<3> Magic\n'
          '<0> Exit\n')


if __name__ == "__main__":
    items = [1, 2, 3, 0]
    chosen_material = int(-1)
    while chosen_material != 0:
        print_menu()
        chosen_material = select_menu_item(items)
        if chosen_material == 1:
            clear_cmd()
            client_operation(FleshFactory())
        elif chosen_material == 2:
            clear_cmd()
            client_operation(CyberneticFactory())
        elif chosen_material == 3:
            clear_cmd()
            client_operation(MagicFactory())

    clear_cmd()
    print('Program shutdown')
    sys.exit()