from smart_home_facade import SmartHomeFacade

def main():
    print("=== Тестирование паттерна Фасад для умного дома ===")

    smart_home = SmartHomeFacade()

    print("\n1. Начальное состояние всех систем:")
    print(smart_home.get_all_systems_status())

    print("\n2. Активация режима 'Я дома':")
    home_results = smart_home.home_mode()
    for result in home_results:
        print(f" - {result}")

    print("\n   Состояние систем после активации режима 'Я дома':")
    print(smart_home.get_all_systems_status())

    print("\n3. Активация режима 'Вечеринка':")
    party_results = smart_home.party_mode()
    for result in party_results:
        print(f" - {result}")

    print("\n   Состояние систем после активации режима 'Вечеринка':")
    print(smart_home.get_all_systems_status())

    print("\n4. Активация режима 'Ночь':")
    night_results = smart_home.night_mode()
    for result in night_results:
        print(f" - {result}")

    print("\n   Состояние систем после активации режима 'Ночь':")
    print(smart_home.get_all_systems_status())

    print("\n5. Активация режима 'Я ухожу':")
    away_results = smart_home.away_mode()
    for result in away_results:
        print(f" - {result}")

    print("\n   Состояние систем после активации режима 'Я ухожу':")
    print(smart_home.get_all_systems_status())

    print("\n=== Тестирование завершено ===")

if __name__ == "__main__":
    main()