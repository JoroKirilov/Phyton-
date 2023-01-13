from Inheritance.shop.food import Food
from Inheritance.shop.product_repo import ProductRepository

stock1 = Food("Butter", "20.01.2023")
print(stock1.quantity)
stock1.increase(100)
print(stock1.quantity)
stock2 = Food("Bread", "21.01.2023")
stock2.decrease(20)
print(stock2.quantity)
shop_repo = ProductRepository()
shop_repo.add(stock1)
shop_repo.add(stock2)
print(shop_repo)
print(shop_repo.product)
