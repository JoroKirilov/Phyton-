class Person:
    def __init__(self, name, age, nationality):
        self.name = name
        self.age = age
        self.natioanlity = nationality

    def set_new_age(self, new_age):
        self.age = new_age

    def __str__(self):
        return f"I am {self.name} and I am {self.natioanlity}"


p1 = Person("Georgi", 35, "Bulgarian")
p1.set_new_age(20)
print(p1.age)
dict_person = p1.__dict__
for key, value in dict_person.items():
    print(key)
    print(value)
print(p1)