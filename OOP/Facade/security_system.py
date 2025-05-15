class SecuritySystem:
    def __init__(self):
        self.alarm_status = "off"
        self.door_locked = True

    def arm_alarm(self):
        self.alarm_status = "armed"
        return "Сигнализация активирована"

    def disarm_alarm(self):
        self.alarm_status = "disarmed"
        return "Сигнализация отключена"

    def lock_doors(self):
        self.door_locked = True
        return "Двери заблокированы"

    def unlock_doors(self):
        self.door_locked = False
        return "Двери разблокированы"

    def get_status(self):
        return f"Сигнализация: {self.alarm_status}, Двери: {'заблокированы' if self.door_locked else 'открыты'}"