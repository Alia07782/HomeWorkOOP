from abc import ABC, abstractmethod
from car import Car, ElectricCar, PetrolCar, HybridCar

class CarFactory(ABC):
    @abstractmethod
    def produce_car(self) -> Car:
        pass


class ElectricCarFactory(CarFactory):
    def produce_car(self) -> ElectricCar:
        return ElectricCar()


class PetrolCarFactory(CarFactory):
    def produce_car(self) -> PetrolCar:
        return PetrolCar()


class HybridCarFactory(CarFactory):
    def produce_car(self) -> HybridCar:
        return HybridCar()