from order_prototype import OrderPrototype

class Order:
    def __init__(self, prototype: OrderPrototype):
        self.order_number = prototype.order_number
        self.products = prototype.products
        self.total_price = prototype.total_price

    def __str__(self):
        return (
            f"Order Number: {self.order_number}\n"
            f"Products: {', '.join(self.products)}\n"
            f"Total Price: {self.total_price:.2f}"
        )