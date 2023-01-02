# Create a class called Vehicle. Upon initialization it
# should receive max_speed (number, optional; 150 by default) and
# mileage (number).
# Create an instance variable called gadgets – empty list by default.

class Vehicle:
    def __init__(self, mileage: int, max_speed=150):
        self.mileage = mileage
        self.max_speed = max_speed
        self.gadgets = []

car = Vehicle(20)
print(car.mileage)
print(car.max_speed)
car.gadgets.append(200)
print(car.gadgets)
