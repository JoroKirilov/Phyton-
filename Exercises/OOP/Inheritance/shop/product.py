class Product:
    def __init__(self, name_of_product: str, quantity: int):
        self.name_of_product = name_of_product
        self.quantity = quantity

    def decrease(self, quantity : int):
        self.quantity -= self.quantity


    def increase(self, quantity: int):
        self.quantity += quantity

    def __repr__(self):
        return f"{self.name_of_product}"
