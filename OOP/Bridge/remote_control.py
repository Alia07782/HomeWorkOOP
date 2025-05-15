class RemoteControl:
    def __init__(self, device: 'Device'):
        self.device = device

    def turn_on(self):
        self.device.turn_on()

    def turn_off(self):
        self.device.turn_off()

    def set_state(self, state):
        self.device.set_state(state)