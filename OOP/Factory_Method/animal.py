from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self) -> str:
        pass


class Lion(Animal):
    def make_sound(self) -> str:
        return "Рычание!"


class Monkey(Animal):
    def make_sound(self) -> str:
        return "Визг!"


class Elephant(Animal):
    def make_sound(self) -> str:
        return "Трубление!"