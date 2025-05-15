from factory import ElectricCarFactory, PetrolCarFactory, HybridCarFactory


def main():
    # Словарь: строка -> фабрика
    factory_mapping = {
        "electric": ElectricCarFactory(),
        "petrol": PetrolCarFactory(),
        "hybrid": HybridCarFactory()
    }

    print("Выберите тип автомобиля: electric, petrol, hybrid или exit для выхода.")

    while True:
        user_input = input("Введите тип автомобиля: ").strip().lower()

        if user_input == "exit":
            print("Выход из программы.")
            break

        if user_input in factory_mapping:
            car = factory_mapping[user_input].produce_car()
            car.drive()
        else:
            print("Неверный ввод! Допустимые значения: electric, petrol, hybrid или exit.")


if __name__ == "__main__":
    main()