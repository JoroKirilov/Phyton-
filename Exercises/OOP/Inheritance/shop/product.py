class Product:
    def __init__(self, name_of_product: str, quantity: int):
        self.name_of_product = name_of_product
        self.quantity = quantity

    def decrease(self, quantity: int):
        if self.quantity >= quantity:
            self.quantity -= quantity
        else:
            print(f"Not enough quantity. Available at moment : {self.quantity}")


    def increase(self, quantity: int):
        self.quantity += quantity

    def __repr__(self):
        return self.name_of_product
