
class Pen:
    def __init__(self, brand: str, color: str, capacity= 10):
        self.brand = brand
        self.color = color
        self.capacity = capacity

    def write(self):
        if self.capacity > 0:
            self.capacity -= 1
            return "Writing..."
        return "No ink"