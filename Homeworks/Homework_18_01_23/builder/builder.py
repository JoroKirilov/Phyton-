from Homework_18_01_23.builder.figures.square import Square
from Homework_18_01_23.builder.figures.triangle import Triangle


class Builder(Square):
    def __init__(self, side: int):
        super().__init__(side)
        self.triangles_list = []

    def build_triangle(self, side1, side2, side3):
        if len(self.triangles_list) == 10:
            print("Builder can make up to 10 triangles only")
            return
        tmp_name = Triangle(side1, side2, side3)
        self.triangles_list.append(tmp_name)


b = Builder(100)
b.build_triangle(4, 6, 6)
b.build_triangle(6, 6, 6)

for triangle in b.triangles_list:
    b.add_triangle_in_square(triangle.get_triangle_area())
print(b.triangles_inside)


