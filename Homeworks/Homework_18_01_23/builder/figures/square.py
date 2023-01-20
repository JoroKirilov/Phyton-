class Square:
    def __init__(self, side: int):
        self.side = side
        self.free_space = side * 4
        self.triangles_inside = 0

    def check_area(self):
        return self.side ** 2

    def check_is_full(self):
        if self.free_space == 0:
            return True
        return False


