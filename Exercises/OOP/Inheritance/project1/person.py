class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Hello {self.name} of type {self.__class__.__name__}"
