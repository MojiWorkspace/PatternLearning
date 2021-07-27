# This program is based on Composite pattern

# Situation: Generate a tree-structure object that describes
# storage contents

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
from random import randint


class Component(ABC):
    @property
    def parent(self) -> Component:
        return self._parent

    @parent.setter
    def parent(self, parent: Component):
        self._parent = parent

    def add(self, component: Component) -> None:
        pass

    def remove(self, component: Component) -> None:
        pass

    def is_composite(self) -> bool:
        return False

    @abstractmethod
    def operation(self) -> str:
        pass


class Box(Component):
    def operation(self) -> str:
        return "\n            -> Leaf: Box"


class Storage(Component):
    def __init__(self) -> None:
        self._children: List[Component] = []

    def add(self, component: Component) -> None:
        self._children.append(component)
        component.parent = self

    def remove(self, component: Component) -> None:
        self._children.remove(component)
        component.parent = None

    def is_composite(self) -> bool:
        return True

    def operation(self) -> str:
        results = []
        for child in self._children:
            results.append(child.operation())
        return f"-> Root: Warehouse {''.join(results)}"


class Section(Storage):
    def operation(self) -> str:
        results = []
        for child in self._children:
            results.append(child.operation())
        return f"\n   -> Branch: Section{''.join(results)}"


class Shelving(Storage):
    def operation(self) -> str:
        results = []
        for child in self._children:
            results.append(child.operation())
        return f"\n       -> Branch: Shelving{''.join(results)}"


# Description of all tree structure is called by one operation
def client_code(component: Component) -> None:
    print(f"\nRESULT:\n\n{component.operation()}", end="")


if __name__ == '__main__':

    # Tree initialization
    storage_tree = Storage()

    # Generating some data
    storage_matrix = [
        [[randint(2, 5) for _ in range(randint(2, 5))]
         for _ in range(randint(2, 5))]
        for _ in range(randint(2, 5))]

    for section in range(len(storage_matrix)):
        sect = Section()
        for shelv in range(len(storage_matrix[section])):
            sh = Shelving()
            for box in range(len(storage_matrix[section][shelv])):
                b = Box()
                sh.add(b)

            sect.add(sh)

        storage_tree.add(sect)

    # Client code call with created tree
    client_code(storage_tree)
