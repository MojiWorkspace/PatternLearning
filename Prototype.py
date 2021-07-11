# This program is based on Prototype pattern
# Python standard lib has the Copy module which used to copy (clone) objects
# Script represents 2 ways for copy: Shallow and Deep copy

# From Python 3.9.6 documentation:
# The difference between shallow and deep copying
# is only relevant for compound objects
# (objects that contain other objects, like lists or class instances):
# A shallow copy constructs a new compound object
# and then (to the extent possible) inserts references into it
# to the objects found in the original.
# A deep copy constructs a new compound object and then,
# recursively, inserts copies into it of the objects found in the original.

# Difference between Shallow and Deep copy you could see from (for example)
# .reference.parent value of each copy (clone)

import copy
import os
import platform
import time


class SelfReferencingEntity:
    def __init__(self):
        self.parent = None

    def set_parent(self, parent):
        self.parent = parent


class ComponentToClone:
    def __init__(self, some_int, object_list, reference):
        self.some_int = some_int
        self.object_list = object_list
        self.reference = reference

    def __copy__(self):
        # Creating copies of nested objects
        object_list = copy.copy(self.object_list)
        reference = copy.copy(self.reference)

        # Cloning the object itself, using the prepared clones of the nested objects
        new = self.__class__(
            self.some_int, object_list, reference
        )
        new.__dict__.update(self.__dict__)

        return new

    def __deepcopy__(self, memo={}):
        # Creating copies of the nested objects.
        object_list = copy.deepcopy(self.object_list, memo)
        reference = copy.deepcopy(self.reference, memo)

        # Cloning the object itself, using the prepared clones of the nested objects
        new = self.__class__(
            self.some_int, object_list, reference
        )
        new.__dict__ = copy.deepcopy(self.__dict__, memo)

        return new


def clear_cmd():
    if platform.system() == 'Linux':
        os.system('clear')
    elif platform.system() == 'Windows':
        os.system('cls')


if __name__ == "__main__":
    clear_cmd()

    # Some list of simple objects
    list_of_objects = [1, {1, 2, 3}, [1, 2, 3]]

    # SelfReference object initialization
    circular_ref = SelfReferencingEntity()

    # ComponentToClone object initialization
    component = ComponentToClone(25, list_of_objects, circular_ref)

    # Reference for SelfReference object set
    circular_ref.set_parent(component)

    clone_number = int(-1)
    while clone_number < 1:
        try:
            clear_cmd()
            clone_number = int(input('Enter the number of clones: '))
            print('\n')
            if clone_number < 1:
                continue
            else:
                for clone in range(clone_number):
                    shallow_copied_component = copy.copy(component)
                    print(f'Shallow copy of \'component\' produced at id: {id(shallow_copied_component.reference.parent)}\n')
                    time.sleep(0.5)

                print('\n')

                for clone in range(clone_number):
                    deep_copied_component = copy.deepcopy(component)
                    print(f'Deep copy of \'component\' produced at id: {id(deep_copied_component.reference.parent)}\n')
                    time.sleep(0.5)

        except ValueError:
            continue
