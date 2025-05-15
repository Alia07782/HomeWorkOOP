from abc import ABC, abstractmethod
from car import Car

class CarBuilder(ABC):
    @abstractmethod
    def set_brand(self):
        pass

    @abstractmethod
    def set_model(self):
        pass

    @abstractmethod
    def set_engine(self):
        pass

    @abstractmethod
    def set_transmission(self):
        pass

    @abstractmethod
    def set_body(self):
        pass

    @abstractmethod
    def get_car(self) -> Car:
        pass
