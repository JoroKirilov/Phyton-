class ProductRepository:
    def __init__(self):
        self.product = []

    def add(self, stock):
        self.product.append(stock)

    def __repr__(self):
        result = ''
        print("Products in shop repo")
        for product in self.product:
            result += f"{product.name_of_product}: {product.quantity}\n"

        return result
