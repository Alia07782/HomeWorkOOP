from builders import CarBuilder

class CarDirector:
    def __init__(self, builder: CarBuilder):
        self.builder = builder

    def construct_car(self):
        self.builder.set_brand()
        self.builder.set_model()
        self.builder.set_engine()
        self.builder.set_transmission()
        self.builder.set_body()
        return self.builder.get_car()