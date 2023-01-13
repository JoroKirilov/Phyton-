from Inheritance.shop.product import Product


class Food(Product):
    def __init__(self, name_of_product, exp_date: str):
        super().__init__(name_of_product, 10)
        self.exp_date = exp_date

