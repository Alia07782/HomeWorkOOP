class LightingSystem:
    def __init__(self):
        self.status = "off"
        self.brightness = 50

    def turn_on(self):
        self.status = "on"
        return "Освещение включено"

    def turn_off(self):
        self.status = "off"
        return "Освещение выключено"

    def set_brightness(self, level):
        self.brightness = level
        return f"Яркость установлена на {level}%"

    def get_status(self):
        return f"Освещение: {self.status}, Яркость: {self.brightness}%"