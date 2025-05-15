from abc import ABC, abstractmethod


class Device(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    @abstractmethod
    def set_state(self, state):
        pass



class TV(Device):
    def turn_on(self):
        print("Включение телевизора")

    def turn_off(self):
        print("Выключение телевизора")

    def set_state(self, channel):
        print(f"Переключение на канал {channel}")



class Light(Device):
    def turn_on(self):
        print("Включение лампочки")

    def turn_off(self):
        print("Выключение лампочки")

    def set_state(self, brightness):
        print(f"Установка яркости лампочки на {brightness}")