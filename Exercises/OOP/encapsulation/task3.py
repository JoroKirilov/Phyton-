class Tv:
    def __init__(self, model: str, password: str):
        self.model = model
        self.password = password
        self.is_on = False
        self.dts = True



    def turn_on_button(self):
        self.is_on = not self.is_on

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        self.__password = value


lg = Tv("c1", "cinemaDream")
lg.password = "gamingDream"
print(lg.password)
lg.dts = False
print(lg.dts)
