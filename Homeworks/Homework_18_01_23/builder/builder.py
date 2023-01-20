from Homework_18_01_23.builder.figures.square import Square
from Homework_18_01_23.builder.figures.triangle import Triangle


class Builder(Square):
    def __init__(self, side: int):
        super().__init__(side)
        self.triangles_list = []

    def __is_valid_triangle(self, a, b, c):
        if a + b > c and a + c > b and b + c > a:
            return True
        else:
            return False

    def get_info_for_triangles(self):
        tmp_str = ''
        for index in range(len(self.triangles_list)):
            tmp_str += f"triangle #{index + 1}: {self.triangles_list[index].kind_of_triangle_by_sides()}"
            tmp_str += "\n"
        return tmp_str

    def build_triangle(self, a, b, c):
        if self.__is_valid_triangle(a, b, c):
            if len(self.triangles_list) == 10:
                print("Builder can make up to 10 triangles only")
                return
            tmp_name = Triangle(a, b, c)
            self.triangles_list.append(tmp_name)
        else:
            print("Not valid triangle sides")

    def add_triangle_in_square(self):
        try:
            tmp_triangle = self.triangles_list.pop()
            triangle_area = tmp_triangle.get_triangle_area()
            if self.free_space >= triangle_area:
                self.free_space -= triangle_area
                self.triangles_inside += 1
                print("Done")
                if self.check_is_full():
                    print("No space left")
            else:
                print("No space for that triangle")
        except IndexError:
            print("No more triangle to add. You need to build some.")


b = Builder(100)
b.build_triangle(10, 20, 20)  # CREATE TRIANGLE WITH BUILDER
b.add_triangle_in_square()  # TRY TO ADD TRIANGLE IN SQUARE
print(b.triangles_inside)  # LOOK HOW MANY TRIANGLE IN SQUARE
b.add_triangle_in_square()  # TRY TO ADD TRIANGLE IN SQUARE, BUT THERE IS NO CREATE TRIANGLE
print(b.check_area())  # GET THE SQUARE AREA
b.build_triangle(20, 20, 20)  # CREATE ANOTHER TRIANGLE
b.build_triangle(10, 10, 10)
b.build_triangle(30, 30, 30)
print(b.get_info_for_triangles())  # LOOK WHAT KIND OF TRIANGLES I BUILD
