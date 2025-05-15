from lighting_system import LightingSystem
from climate_control import ClimateControl
from security_system import SecuritySystem
from multimedia_system import MultimediaSystem

class SmartHomeFacade:
    def __init__(self):
        self.lighting = LightingSystem()
        self.climate = ClimateControl()
        self.security = SecuritySystem()
        self.multimedia = MultimediaSystem()

    def home_mode(self):
        results = [
            self.lighting.turn_on(),
            self.lighting.set_brightness(70),
            self.climate.set_temperature(22),
            self.climate.set_mode("comfort"),
            self.security.disarm_alarm(),
            self.security.unlock_doors()
        ]
        return results

    def away_mode(self):
        results = [
            self.lighting.turn_off(),
            self.multimedia.stop_music(),
            self.security.lock_doors(),
            self.security.arm_alarm()
        ]
        return results

    def party_mode(self):
        results = [
            self.lighting.turn_on(),
            self.lighting.set_brightness(40),
            self.climate.set_temperature(24),
            self.climate.set_mode("party"),
            self.multimedia.play_music("Party Hits"),
            self.multimedia.set_volume(60)
        ]
        return results

    def night_mode(self):
        results = [
            self.lighting.turn_off(),
            self.multimedia.stop_music(),
            self.climate.set_temperature(18),
            self.climate.set_mode("night"),
            self.security.arm_alarm()
        ]
        return results

    def get_all_systems_status(self):
        return (
            self.lighting.get_status() + "\n" +
            self.climate.get_status() + "\n" +
            self.security.get_status() + "\n" +
            self.multimedia.get_status()
        )