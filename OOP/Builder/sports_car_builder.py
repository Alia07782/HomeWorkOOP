from car import Car
from components import Engine
from components import Transmission
from components import Body
from builders import CarBuilder

class SportsCarBuilder(CarBuilder):
    def __init__(self):
        self.car = Car()

    def set_brand(self):
        self.car.brand = "Ваз"

    def set_model(self):
        self.car.model = "2114"

    def set_engine(self):
        self.car.engine = Engine("Турбированный", 650)

    def set_transmission(self):
        self.car.transmission = Transmission("Роботизированная")

    def set_body(self):
        self.car.body = Body("Спорткар", "Серебристый")

    def get_car(self):
        return self.car