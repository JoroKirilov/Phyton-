class RadioConnector:
    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model
        self.volume_level = 10

    def show_volume_level(self):
        print(f"Current volume level is : {self.volume_level}")

    def volume_up(self, level_up: int):
        self.volume_level += level_up
        self.show_volume_level()

    def volume_down(self, level_down: int):
        self.volume_level -= level_down
        if self.volume_level <= level_down:
            self.volume_level = 0
        self.show_volume_level()

    def mute(self):
        self.volume_level = 0
        print("MUTE")


