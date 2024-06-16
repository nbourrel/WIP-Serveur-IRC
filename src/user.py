class User:
    def __init__(self, nickname):
        self.nickname = nickname
        self.channels = []  # List of channels the user has joined
        self.modes = []

    def add_mode(self, mode):
        if mode not in self.modes:
            self.modes.append(mode)

    def remove_mode(self, mode):
        if mode in self.modes:
            self.modes.remove(mode)

    def list_modes(self):
        return self.modes