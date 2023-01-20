from Homework_18_01_23.builder.custom_exeptions.exeptions import NoFreeSpace


class Square:
    def __init__(self, side: int):
        self.side = side
        self.free_space = side * 4
        self.triangles_inside = 0

    def check_area(self):
        return self.side ** 2

    def add_triangle_in_square(self, triangle_area: int):
        if self.free_space > triangle_area:
            self.free_space -= triangle_area
            self.triangles_inside += 1
            print("Done")
            if self.__check_is_full():
                print("No space for that triangle")
        else:
            print("No more space")

    def __check_is_full(self):
        if self.free_space == 0:
            return True
        return False


