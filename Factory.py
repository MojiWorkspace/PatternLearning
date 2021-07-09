# All information about program you can read from main menu

from abc import ABC, abstractmethod
import os
import sys
import platform
import time
import datetime


# Abstract factory class. Used to declare default methods for specific factories
class Factory(ABC):
    @abstractmethod
    def factory_method(self):
        pass

    def default_operation(self):
        product = self.factory_method()
        result = f"Factory: Unit is ready - {product.operation()}"
        return result


# Abstract window class. Used to declare default methods for specific windows
class Window(ABC):
    @abstractmethod
    def operation(self):
        pass


# Conveyor that produces rectangular windows
class RectangularWindowConveyor(Factory):
    def factory_method(self):
        return RectangularWindow()


# Conveyor that produces triangular windows
class TriangularWindowConveyor(Factory):
    def factory_method(self):
        return TriangularWindow()


# Conveyor that produces circular windows
class CircularWindowConveyor(Factory):
    def factory_method(self):
        return CircularWindow()


class RectangularWindow(Window):
    def operation(self):
        return '{Rectangular Window}'


class TriangularWindow(Window):
    def operation(self):
        return '{Triangular Window}'


class CircularWindow(Window):
    def operation(self):
        return '{Circular Window}'


# Client's order
class Order:
    def __init__(self):
        self.rect = 0
        self.tria = 0
        self.circ = 0

    def show_details(self):
        print(f'\nOrder details:\n'
              f'Rectangular windows - {self.rect}\n'
              f'Triangular windows - {self.tria}\n'
              f'Circular windows - {self.circ}\n')


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


def count_input(item):
    count = int(-1)
    while count < 0 or count > 100:
        try:
            count = int(input(f'\n({item}) Enter count: '))
            if count < 0 or count > 100:
                print(f'\nCount \"{count}\" is not available\n')
        except ValueError:
            print('\nInput value error\nNot an integer\n\nPlease repeat the input\n\n')

    return count


# Operation for client (Execute producing process)
def client_operation(factory: Factory):
    print(f'{factory.default_operation()}')


def print_main_menu():
    clear_cmd()
    print('#############\n# MAIN MENU #\n#############\n\n'
          'Please choose the operation\n'
          'Confirm your choice by <Enter>\n\n'
          '<1> Open the description\n'
          '<2> Start the factory\n'
          '<0> Exit\n')


def print_order_menu():
    clear_cmd()
    print('##############\n# ORDER MENU #\n##############\n\n'
          '<1> Rectangular windows count (default 0)\n'
          '<2> Triangular windows count (default 0)\n'
          '<3> Circular  windows count (default 0)\n'
          '<4> Order details\n'
          '<5> Confirm\n'
          '<0> Back\n')


def open_description():
    clear_cmd()
    print('This program is based on Factory pattern.\n\n'
          'Script represents the work of the factory\n'
          'that produces windows of different shapes:\n'
          'Rectangular, Triangular, Circular.\n\n'
          'The client (user) makes an order:\n'
          '- Shape\n'
          '- Count\n\n'
          'One order could contain a number (0 - 100) of windows of each available shape.\n'
          'Before order confirmation you can read all details.\n'
          'After order confirmation the producing process will be shown.\n\n'
          'Press <Enter> to return to main menu')


# Console UI and Logic
def client_menu():
    print_main_menu()
    items = [1, 2, 0]
    chosen_operation = int(-1)
    while chosen_operation != 0:
        chosen_operation = select_menu_item(items)
        if chosen_operation == 1:
            open_description()
            input()
            print_main_menu()
        elif chosen_operation == 2:
            def start_factory_menu():
                order = Order()
                factory_menu_items = [1, 2, 3, 4, 5, 0]
                print_order_menu()
                chosen_operation = int(-1)
                while chosen_operation != 5 and chosen_operation != 0:
                    chosen_operation = select_menu_item(factory_menu_items)
                    if chosen_operation == 1:
                        count = count_input(1)
                        order.rect = count
                        print_order_menu()
                    elif chosen_operation == 2:
                        count = count_input(2)
                        order.tria = count
                        print_order_menu()
                    elif chosen_operation == 3:
                        count = count_input(3)
                        order.circ = count
                        print_order_menu()
                    elif chosen_operation == 4:
                        if order.rect == 0 and order.tria == 0 and order.circ == 0:
                            print('\nYour order is empty\nPress <Enter> to continue')
                            input()
                            print_order_menu()
                        else:
                            order.show_details()
                            print('Press <Enter to continue>')
                            input()
                            print_order_menu()

                if chosen_operation == 5:
                    if order.rect == 0 and order.tria == 0 and order.circ == 0:
                        print('\nYour order is empty\nPress <Enter> to continue')
                        input()
                        start_factory_menu()
                    else:
                        clear_cmd()
                        order.show_details()
                        print('Press <Enter> to start the Factory')
                        input()
                        print('Producing...\n')
                        if order.rect > 0:
                            for window in range(order.rect):
                                client_operation(RectangularWindowConveyor())
                                time.sleep(0.25)
                            print('\n')
                        if order.tria > 0:
                            for window in range(order.tria):
                                client_operation(TriangularWindowConveyor())
                                time.sleep(0.25)
                            print('\n')
                        if order.circ > 0:
                            for window in range(order.circ):
                                client_operation(CircularWindowConveyor())
                                time.sleep(0.25)
                            print('\n')
                        print(f'{current_datetime()}\nProducing complete\n\nPress <Enter> to continue')
                        input()
                        print_main_menu()

                elif chosen_operation == 0:
                    print_main_menu()

            start_factory_menu()

    clear_cmd()
    print('Program shutdown')
    sys.exit()


if __name__ == "__main__":
    client_menu()