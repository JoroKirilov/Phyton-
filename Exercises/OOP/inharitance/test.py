class Person:
    def __init__(self, name, age):
        if len(name.split()) < 2:
            raise Exception("shoud enter two names!")
        res = [len(n) >= 2 for n in name.split()]
        if not all(res):
            raise Exception("Each name must be at least two characters !")
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hello, from {self.name}")


class Employer(Person):
    def __init__(self, name, age, salary, ids):
        super().__init__(name, age)
        self.salary = salary
        self.ids = ids


class Manager(Employer):
    def __init__(self, name, age, salary, ids, bonus):
        super().__init__(name, age, salary, ids)
        self.bonus = bonus


manager1 = Manager('Georgi Kirilov', 35, 4500, 65, 2000)
print(manager1.salary)


# class Student(Person):
#     pass
#
#
# student1 = Student('Georgi Kirilov', 69)
# student1.name = 'GEORGI'
# print(student1.name)
