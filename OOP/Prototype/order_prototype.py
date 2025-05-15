import copy

class OrderPrototype:
    def __init__(self):
        self.order_number = None
        self.products = []
        self.total_price = 0.0

    def clone(self):
        return copy.deepcopy(self)