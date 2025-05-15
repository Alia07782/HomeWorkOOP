from car import Car
from components import Engine
from components import Transmission
from components import Body
from builders import CarBuilder

class SUVBuilder(CarBuilder):
    def __init__(self):
        self.car = Car()

    def set_brand(self):
        self.car.brand = "Рено"

    def set_model(self):
        self.car.model = "Логан"

    def set_engine(self):
        self.car.engine = Engine("Бензиновый", 260)

    def set_transmission(self):
        self.car.transmission = Transmission("Механика")

    def set_body(self):
        self.car.body = Body("Внедорожник", "Черный")

    def get_car(self):
        return self.car