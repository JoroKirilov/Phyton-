products = [product for product in input().split()]
searching_stock = [stocks for stocks in input().split()]
stock_dict = {}
for index in range(0, len(products), 2):
    stock_dict[products[index]] = int(products[index + 1])
for element in searching_stock:
    if element in stock_dict:
        print(f"We have {stock_dict[element]} of {element} left")
    else:
        print(f"Sorry, we don't have {element}")
