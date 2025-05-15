class MultimediaSystem:
    def __init__(self):
        self.volume = 30
        self.current_track = "None"

    def play_music(self, track="Relaxing Jazz"):
        self.current_track = track
        return f"Воспроизведение музыки: {track}"

    def stop_music(self):
        self.current_track = "None"
        return "Музыка остановлена"

    def set_volume(self, level):
        self.volume = level
        return f"Громкость установлена на {level}%"

    def get_status(self):
        return f"Музыка: {self.current_track}, Громкость: {self.volume}%"