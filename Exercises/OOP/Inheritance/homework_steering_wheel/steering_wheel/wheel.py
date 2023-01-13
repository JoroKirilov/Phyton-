from Inheritance.homework_steering_wheel.steering_wheel.airbag import Airbag
from Inheritance.homework_steering_wheel.steering_wheel.radio_connector import RadioConnector

class SteeringWheel:
    def __init__(
        self,
        color: str,
        diameter: int,
        material="cheap",
        form="circle",
        airbag=None,
        volume_control=False,
        radio_connector=None,
    ):
        self.position = 0
        self.color = color
        self.diameter = diameter
        self.material = material
        self.form = form
        self.airbag = airbag

        # Add logic to ensure that you have radio_connector if volume_control is True.
        self.radio_connector = self.__ensure_radio_connecter_if_needed(
            volume_control, radio_connector,
        )

    def __ensure_radio_connecter_if_needed(self, volume_control, radio_connector):
        if not volume_control:
            return
        if radio_connector is None:
            raise Exception("Missing radio connector")
        return radio_connector

    def steer_left(self):
        self.position -= 10
        self.__get_position()
        self.auto_steer_to_initial()

    def steer_right(self):
        self.position += 10
        self.__get_position()
        self.auto_steer_to_initial()

    def auto_steer_to_initial(self):
        self.position = 0
        self.__get_position()

    def __get_position(self):
        print(f"Wheel steered to {self.position}")

    def increase_volume(self, level_up: int):
        if self.radio_connector:
            self.radio_connector.volume_up(level_up)

    def decrease_volume(self, level_down: int):
        if self.radio_connector:
            self.radio_connector.volume_down(level_down)

    def show_volume_music_level(self):
        self.radio_connector.show_volume_level()


airbag1 = Airbag("Safe system v2")
radio_connector1 = RadioConnector("JVC", "TR1021")


my_custom_steering_wheel = SteeringWheel("Black and white", 34, "Carbon", "Ellipse",
                                         airbag=airbag1, volume_control=True, radio_connector=radio_connector1)

print(f"Color   : {my_custom_steering_wheel.color}")
print(f"Form    : {my_custom_steering_wheel.form}")
print(f"Diameter: {my_custom_steering_wheel.diameter}")
print(f"Material: {my_custom_steering_wheel.material}")
my_custom_steering_wheel.airbag.check_airbag_system()
my_custom_steering_wheel.show_volume_music_level()
my_custom_steering_wheel.increase_volume(100)
my_custom_steering_wheel.decrease_volume(200)
my_custom_steering_wheel.radio_connector.mute()
my_custom_steering_wheel.airbag.deactivate_airbag()
my_custom_steering_wheel.airbag.deactivate_airbag()
my_custom_steering_wheel.airbag.active_airbag()
