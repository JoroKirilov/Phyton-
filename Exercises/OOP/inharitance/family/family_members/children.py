from family.family_members.parents import Father, Mother


class Boy(Mother, Father):
    def __init__(self, name):
        self.name = name
        Mother.__init__(self)
        Father.__init__(self)


    def playing_the_guitar(self, name):
        return f"Music is playing...{name}...."