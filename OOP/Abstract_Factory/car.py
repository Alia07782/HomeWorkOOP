from abc import ABC, abstractmethod

class Car(ABC):
    @abstractmethod
    def drive(self) -> None:
        pass


class ElectricCar(Car):
    def drive(self) -> None:
        print("Driving an electric car.")


class PetrolCar(Car):
    def drive(self) -> None:
        print("Driving a petrol car.")


class HybridCar(Car):
    def drive(self) -> None:
        print("Driving a hybrid car.")