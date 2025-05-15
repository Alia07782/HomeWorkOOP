class ClimateControl:
    def __init__(self):
        self.temperature = 20
        self.mode = "auto"

    def set_temperature(self, temp):
        self.temperature = temp
        return f"Температура установлена на {temp}°C"

    def set_mode(self, mode):
        self.mode = mode
        return f"Режим климата изменен на {mode}"

    def get_status(self):
        return f"Климат: {self.temperature}°C, Режим: {self.mode}"