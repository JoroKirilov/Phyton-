class Sides:
    def __init__(self, a: int, b: int, c: int):
        self.a = a
        self.b = b
        self.c = c


class Triangle(Sides):
    def __init__(self, a: int, b: int, c: int):
        super().__init__(a, b, c)
        self.area = 0

    def kind_of_triangle_by_sides(self):
        if self.a == self.b == self.c:
            return "equilateral triangle"
        elif self.a == self.b or self.a == self.c or self.b == self.c:
            return "isosceles triangle"
        else:
            return "scalene triangle"

    def get_triangle_area(self):
        s = (self.a + self.b + self.c) / 2
        area = (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5
        return area

    def __repr__(self):
        return self.kind_of_triangle_by_sides()

