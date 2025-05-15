class GameSettings:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(GameSettings, cls).__new__(cls)
        return cls._instance

    def __init__(self):
           if not hasattr(self, 'initialized'):
            self.volume = 50
            self.difficulty = "Normal"
            self.initialized = True