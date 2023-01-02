# Create a class called Car. Upon initialization it should receive a name, model and engine (all strings).
# Create a method called get_info() which will return a string in the following format:
# "This is {name} {model} with engine {engine}".

class Car:
    def __init__(self, name: str, model: str, engine: str):
        self.name = name
        self.model = model
        self.engine = engine

    def get_info(self):
        return f"This is {self.name} {self.model} with engine {self.engine}"


car = Car("audi", "s6", "4.6")
print(car.get_info())
