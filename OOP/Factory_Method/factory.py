from abc import ABC, abstractmethod
from animal import Animal, Lion, Monkey, Elephant

class AnimalFactory(ABC):
    @abstractmethod
    def create_animal(self) -> Animal:
        pass


class LionFactory(AnimalFactory):
    def create_animal(self) -> Lion:
        return Lion()


class MonkeyFactory(AnimalFactory):
    def create_animal(self) -> Monkey:
        return Monkey()


class ElephantFactory(AnimalFactory):
    def create_animal(self) -> Elephant:
        return Elephant()