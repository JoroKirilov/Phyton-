class Person:
    def check_person(self):
        pass


class Student(Person):
    def __init__(self, age: int):
        super().__init__()
        self.age = age

    def check_age(self):
        if self.age > 80:
            return False
        return True

    def check_person(self):
        return self.check_age()


class Teacher(Person):
    def __init__(self, skill):
        super().__init__()
        self.skill = skill

    def check_skill(self):
        if self.skill == "master":
            return True
        return False

    def check_person(self):
        return self.check_skill()


list1 = [
    Teacher("master"),
    Teacher("not master yet"),
    Student(34),
    Student(45),
    Student(89),
    Student(81)
]

for persons in list1:
    print(persons.check_person())

