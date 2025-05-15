from components import Engine
from components import Transmission
from components import Body

class Car:
    def __init__(self):
        self.brand = None
        self.model = None
        self.engine: Engine = None
        self.transmission: Transmission = None
        self.body: Body = None

    def __str__(self):
        return (
            f"Марка: {self.brand}\n"
            f"Модель: {self.model}\n"
            f"Двигатель: {self.engine}\n"
            f"Коробка передач: {self.transmission}\n"
            f"Кузов: {self.body}"
        )