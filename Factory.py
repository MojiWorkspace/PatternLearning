from abc import ABC, abstractmethod
import os
import sys


def client_menu():
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

    def print_main_menu():
        items = [1, 2, 3, 0]
        os.system('cls')
        print('#############\n  MAIN MENU  \n#############\n\n'
              'Please choose the operation\n'
              'Confirm your choice by <Enter>\n\n'
              '<1> Open the description\n'
              '<2> Start the factory\n'
              '<3> View order list\n'
              '<0> Exit\n')
        chosen_operation = select_menu_item(items)
        if chosen_operation == 1:
            def open_description():
                os.system('cls')
                print('This program is based on Factory pattern.\n\n'
                      'Script represent the work of the factory\n'
                      'that produces windows of different shapes:\n'
                      'Rectangular, Triangular, Circular.\n\n'
                      'The client (user) makes an order:\n'
                      '- Shape\n'
                      '- Count\n\n'
                      'One order could contain any number of windows of each available shape.\n'
                      'Before order confirmation you can read all details and change your order if it needed.\n'
                      'After order confirmation the producing process will be shown.\n\n'
                      'You can view your order history in main menu.\n\n'
                      'Press <Enter> to return to main menu')

            open_description()

            chosen_operation = input()
            if chosen_operation == '':
                print_main_menu()

        elif chosen_operation == 2:
            def start_factory_menu():
                os.system('cls')
                print('Work in progress\n\nPress <Enter> to return to main menu')

            start_factory_menu()

            chosen_operation = input()
            if chosen_operation == '':
                print_main_menu()

        elif chosen_operation == 3:
            def show_order_list():
                os.system('cls')
                print('Work in progress\n\nPress <Enter> to return to main menu')

            show_order_list()
            chosen_operation = input()
            if chosen_operation == '':
                print_main_menu()

        elif chosen_operation == 0:
            os.system('cls')
            print('Program shutdown')
            sys.exit()

    print_main_menu()


if __name__ == "__main__":
    client_menu()