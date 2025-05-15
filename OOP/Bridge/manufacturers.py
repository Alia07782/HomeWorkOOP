from device import TV, Light

# Телевизоры
class SonyTV(TV):
    def turn_on(self):
        print("Sony TV: Включение")

    def turn_off(self):
        print("Sony TV: Выключение")

    def set_state(self, channel):
        print(f"Sony TV: Переключение на канал {channel}")


class SamsungTV(TV):
    def turn_on(self):
        print("Samsung TV: Включение")

    def turn_off(self):
        print("Samsung TV: Выключение")

    def set_state(self, channel):
        print(f"Samsung TV: Переключение на канал {channel}")


# Лампочки
class PhilipsLight(Light):
    def turn_on(self):
        print("Philips Light: Включение")

    def turn_off(self):
        print("Philips Light: Выключение")

    def set_state(self, brightness):
        print(f"Philips Light: Установка яркости {brightness}")


class IKEALight(Light):
    def turn_on(self):
        print("IKEA Light: Включение")

    def turn_off(self):
        print("IKEA Light: Выключение")

    def set_state(self, brightness):
        print(f"IKEA Light: Установка яркости {brightness}")