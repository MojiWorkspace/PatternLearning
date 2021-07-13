# This program is based on Singleton pattern

import os
import platform
from threading import Lock, Thread


# Metaclass for simple singleton
class SimpleSingletonMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        # If there is no object of a class, then create singleton
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


# Singleton class, with specified metaclass
class SimpleSingleton(metaclass=SimpleSingletonMeta):
    # Params &
    # Methods of singleton
    def some_business_logic(self):
        pass


# Metaclass for singleton (for multiprocess)
class MultiProcSingletonMeta(type):
    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                # If there is no object of a class, then create singleton
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
            return cls._instances[cls]


# Singleton class, with specified metaclass (for multiprocess)
class MultiProcSingleton(metaclass=MultiProcSingletonMeta):
    # Some string value for make sure that singleton is working correctly
    value: str = None

    def __init__(self, value: str) -> None:
        self.value = value

    def some_business_logic(self):
        pass


def test_singleton(value: str) -> None:
    singleton = MultiProcSingleton(value)
    print(singleton.value)


def clear_cmd():
    if platform.system() == 'Linux':
        os.system('clear')
    elif platform.system() == 'Windows':
        os.system('cls')


# Client code
if __name__ == "__main__":
    clear_cmd()
    # Calling the class constructor for several times
    print('Singleton example:')
    client1 = SimpleSingleton()
    client2 = SimpleSingleton()
    client3 = SimpleSingleton()
    # Objects s1, s2, s3 have the same reference
    # to the first produced singleton object (client1)
    # New objects didn't create by client2, client3
    print(f'\nclient1 id: {id(client1)}\nclient2 id: {id(client2)}\nclient3 id: {id(client3)}')

    # Singleton for some processes
    print('\nSingleton example with multiprocess:\n')
    process1 = Thread(target=test_singleton, args=("Singleton: First Call",))
    process2 = Thread(target=test_singleton, args=("Singleton: Second Call",))
    process3 = Thread(target=test_singleton, args=("Singleton: Third Call",))
    process1.start()
    process2.start()
    process3.start()
    # Each process has unique id
    # But singleton object is still equal for all processes
    print(f'\nprocess1 id: {id(process1)}\n'
          f'process2 id: {id(process2)}\n'
          f'process3 id: {id(process3)}')
