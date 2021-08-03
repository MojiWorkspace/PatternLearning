# This program is based on Decorator pattern

# Situation: we have figures - male and female
# and decorators (clothes)
# client have to 'configure' chosen figure himself


class Figure:
    def show_look(self) -> str:
        pass


class MaleFigure(Figure):
    def show_look(self) -> str:
        return 'Male figure'


class FemaleFigure(Figure):
    def show_look(self) -> str:
        return 'Female figure'


class Decorator(Figure):
    def __init__(self, component: Figure) -> None:
        self._component = component

    @property
    def component(self) -> str:
        return self._component

    def show_look(self) -> str:
        return self._component.show_look()


class Underwear(Decorator):
    def show_look(self) -> str:
        return f'\nUnderwear -> is dressed on top of the -> {self.component.show_look()}'


class Sweater(Decorator):
    def show_look(self) -> str:
        return f'\nSweater-> is dressed on top of the -> {self.component.show_look()}'


class Coat(Decorator):
    def show_look(self) -> str:
        return f'\nCoat -> is dressed on top of the -> {self.component.show_look()}'


class Jeans(Decorator):
    def show_look(self) -> str:
        return f'\nJeans -> is dressed on top of the -> {self.component.show_look()}'


class Shorts(Decorator):
    def show_look(self) -> str:
        return f'\nShorts -> is dressed on top of the -> {self.component.show_look()}'


def client_code(component: Figure) -> None:
    print(f"\nRESULT: {component.show_look()}")


if __name__ == "__main__":
    fem_fig = FemaleFigure()
    print("We've got a simple female figure:")
    client_code(fem_fig)

    print("\nLet's make some male figure with \'decorators\':")
    male_fig = MaleFigure()

    underwear = Underwear(male_fig)
    jeans = Jeans(underwear)
    coat = Coat(jeans)

    client_code(coat)

    print('\nLet\'s dress up our female figure in some way with \'decorators\'...')

    shorts = Shorts(fem_fig)
    sweater = Sweater(shorts)
    coat1 = Coat(sweater)
    coat2 = Coat(coat1)
    underwear2 = Underwear(coat2)

    client_code(underwear2)
