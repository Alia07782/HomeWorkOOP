from sedan_builder import SedanBuilder
from suv_builder import SUVBuilder
from sports_car_builder import SportsCarBuilder
from director import CarDirector

if __name__ == "__main__":
    print(" Создание седана ")
    sedan_builder = SedanBuilder()
    director = CarDirector(sedan_builder)
    sedan = director.construct_car()
    print(sedan)

    print("\nСоздание внедорожника")
    suv_builder = SUVBuilder()
    director = CarDirector(suv_builder)
    suv = director.construct_car()
    print(suv)

    print("\nСоздание спорткара")
    sports_car_builder = SportsCarBuilder()
    director = CarDirector(sports_car_builder)
    sports_car = director.construct_car()
    print(sports_car)