from coffee import Coffee, MilkDecorator, ChocolateDecorator, CaramelDecorator

def main():
    basic_coffee = Coffee()
    print(basic_coffee.get_description())
    print(basic_coffee.get_cost())

    milk_coffee = MilkDecorator(basic_coffee)
    print(milk_coffee.get_description())
    print(milk_coffee.get_cost())

    chocolate_milk_coffee = ChocolateDecorator(milk_coffee)
    print(chocolate_milk_coffee.get_description())
    print(chocolate_milk_coffee.get_cost())

    caramel_chocolate_milk_coffee = CaramelDecorator(chocolate_milk_coffee)
    print(caramel_chocolate_milk_coffee.get_description())
    print(caramel_chocolate_milk_coffee.get_cost())

if __name__ == "__main__":
    main()