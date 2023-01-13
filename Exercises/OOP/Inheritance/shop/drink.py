from Inheritance.shop.product import Product


class Drink(Product):
    def __init__(self, name_of_product: str, quantity: int):
        super().__init__(name_of_product, quantity=15)
