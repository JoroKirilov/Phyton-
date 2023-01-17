from human import Human


class Person(Human):
    def __init__(self, name, age, *args):
        super().__init__(*args)
        self.name = name
        self.age = age

    def walk(self):
        print(f"{self.name} has passed 100 meters.")


# person = Person("Male", 185, "Pesho")
# # person.walk()
# print(person.gender)
# print(person.height)
# print(person.name)
# print(person.age)