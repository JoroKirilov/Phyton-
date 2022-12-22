class Person():
    def __init__(self, first_name, last_name, age=0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def say_hi(self):
        print(f"Say hello {self.last_name}")


georgi = Person("Georgi", "Kirilov", 35)
str = georgi.first_name
num = georgi.age
print(num)
georgi.say_hi()