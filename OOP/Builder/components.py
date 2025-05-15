class Engine:
    def __init__(self, engine_type, power):
        self.engine_type = engine_type
        self.power = power

    def __str__(self):
        return f"{self.engine_type}, {self.power} л.с."
class Transmission:
    def __init__(self, transmission_type):
        self.transmission_type = transmission_type

    def __str__(self):
        return self.transmission_type
class Body:
    def __init__(self, body_type, color):
        self.body_type = body_type
        self.color = color

    def __str__(self):
        return f"{self.body_type}, Цвет: {self.color}"