from car import Car
from components import Engine
from components import Transmission
from components import Body
from builders import CarBuilder

class SedanBuilder(CarBuilder):
    def __init__(self):
        self.car = Car()

    def set_brand(self):
        self.car.brand = "Шкода"

    def set_model(self):
        self.car.model = "Актавия"

    def set_engine(self):
        self.car.engine = Engine("Бензиновый", 200)

    def set_transmission(self):
        self.car.transmission = Transmission("Автоматическая")

    def set_body(self):
        self.car.body = Body("Седан", "Серый")

    def get_car(self):
        return self.car