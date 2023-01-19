class Person:
    def __init__(self, age=0):
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 18:
            self.__age = 18
        else:
            self.__age = value

p = Person(13)
print(p.age)
p.age = 14
print(p.age)
