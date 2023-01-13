class Hero:
    def __init__(self, nickname: str, exp: int):
        self.nickname = nickname
        self.exp = exp

    def print_info(self):
        return f"{self.nickname} of type {self.__class__.__name__} is ready for fight"


h = Hero("GE", 23)
sd = h.__str__()
print(sd)