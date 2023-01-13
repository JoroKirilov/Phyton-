from Inheritance.project2.hero import Hero


class Wizard(Hero):
    def __init__(self, nickname, exp):
        super().__init__(nickname, exp)
