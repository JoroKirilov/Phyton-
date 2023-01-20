# Pen Pen should have brand, ink color and capacity (int) as vital attributes.
# It should allow writing. You can make a functionality to the Student class,
# in order to allow storing Pen instances withing.
# Professor should be able to have a very special Pen, think about this
from Homework_18_01_23.pen.pen import Pen


class Student:
    def __init__(self, fac_number: int, first_name: str, last_name: str, pen: Pen):
        self.fac_number = fac_number
        self.first_name = first_name
        self.last_name = last_name
        self.pen = pen


pen1 = Pen("Sheider", "blue", 20)
student1= Student(143543543, "Georgi", "Kirilov", pen1)
print(student1.pen.write())
print(student1.pen.capacity)