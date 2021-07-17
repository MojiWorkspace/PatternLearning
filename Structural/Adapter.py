# This program is based on Adapter pattern
# Situation: Car need adapters for riding rails, sea and sky.


# Car moves by wheels by default
class RideRoad:
    def get_wheels(self):
        print('\nCar is riding the road by wheels now')


class RideRails:
    def get_trainwheels(self):
        print('\nCar is riding the rails by train wheels now')


class RideSea:
    def get_ski(self):
        print('\nCar is riding the sea by ski now')


class RideSky:
    def get_wings(self):
        print('\nCar is riding the sky by wings now')


# Adapter for wheels -> rails
class RailsAdapter:
    def __init__(self):
        self._rail_ad = RideRails()

    def get_wheels(self):
        self._rail_ad.get_trainwheels()


# Adapter for wheels -> ski
class SeaAdapter:
    def __init__(self):
        self._sea_ad = RideSea()

    def get_wheels(self):
        self._sea_ad.get_ski()


# Adapter for wheels -> wings
class SkyAdapter:
    def __init__(self):
        self._sky_ad = RideSky()

    def get_wheels(self):
        self._sky_ad.get_wings()


# Car class
class UserCar:
    def __init__(self, wheels):
        self.wheels = wheels

    def connect(self):
        self.wheels.get_wheels()


if __name__ == '__main__':

    # Car with common wheels to ride on a road
    wheels = RideRoad()
    car = UserCar(wheels)
    car.connect()

    # Car with adapter for wheels to ride rails
    rails_ad = RailsAdapter()
    car = UserCar(rails_ad)
    car.connect()

    # Car with adapter for wheels to ride a sea
    sea_ad = SeaAdapter()
    car = UserCar(sea_ad)
    car.connect()

    # Car with adapter for wheels to ride the sky
    sky_ad = SkyAdapter()
    car = UserCar(sky_ad)
    car.connect()
    