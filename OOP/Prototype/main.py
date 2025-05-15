from order_prototype import OrderPrototype
from order import Order

if __name__ == "__main__":

    prototype_order = OrderPrototype()
    prototype_order.order_number = 1001
    prototype_order.products = ["Product A", "Product B", "Product C"]
    prototype_order.total_price = 150.00


    order1 = Order(prototype_order.clone())
    order1.order_number = 1002
    order1.total_price = 200.00


    order2 = Order(prototype_order.clone())
    order2.order_number = 1003
    order2.products.append("Product D")


    print("Order 1:")
    print(order1)

    print("\nOrder 2:")
    print(order2)