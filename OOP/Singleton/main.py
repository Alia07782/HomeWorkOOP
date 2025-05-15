from game_settings import GameSettings


settings1 = GameSettings()
settings2 = GameSettings()


print(settings1 is settings2)


settings1.volume = 70
settings1.difficulty = "Hard"


print(settings2.volume)
print(settings2.difficulty)