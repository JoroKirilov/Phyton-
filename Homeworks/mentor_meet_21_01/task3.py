class Person:
    def __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        if len(self.__name) > 5:
            return self.__age


p = Person("jOROff", 35)

print(p.get_age())
