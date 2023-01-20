class Sides:
    def __init__(self, side1: int, side2: int, side3: int):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3


class Triangle(Sides):
    def __init__(self, side1: int, side2: int, side3: int):
        super().__init__(side1, side2, side3)

    def kind_of_triangle_by_sides(self):
        if self.side1 == self.side2 == self.side3:
            print("equilateral triangle")
        elif self.side1 == self.side2 or self.side1 == self.side3 or self.side2 == self.side3:
            print("isosceles triangle")
        else:
            print("scalene triangle")

    def get_triangle_area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        area = (s * (s - self.side1) * (s - self.side2) * (s - self.side3)) ** 0.5
        return area

    def __repr__(self):
        self.kind_of_triangle_by_sides()
        return "---triangle is kind of"
