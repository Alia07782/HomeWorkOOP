from factory import LionFactory, MonkeyFactory, ElephantFactory

def interact_with_animal(factory):
    animal = factory.create_animal()
    print(f"Звук: {animal.make_sound()}")


def main():
    factory_mapping = {
        "lion": LionFactory(),
        "monkey": MonkeyFactory(),
        "elephant": ElephantFactory()
    }

    print("Введите тип животного (lion, monkey, elephant) или 'exit' для выхода.")

    while True:
        user_input = input("Введите имя животного: ").strip().lower()

        if user_input == "exit":
            print("Выход из программы.")
            break

        if user_input in factory_mapping:
            interact_with_animal(factory_mapping[user_input])
        else:
            print("Неверный ввод! Допустимые значения: lion, monkey, elephant или 'exit'.")
if __name__ == "__main__":
    main()