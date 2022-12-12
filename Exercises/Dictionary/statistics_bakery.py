my_bakery = {}
while True:
    delivery_info = input().split(": ")
    if delivery_info[0] == 'statistics':
        break
    stocks = delivery_info[0]
    quantity = int(delivery_info[1])
    my_bakery.setdefault(stocks, 0)
    my_bakery[stocks] += quantity
print("Products in stock:")

for key, value in my_bakery.items():
    print(f"- {key}: {value}")

print(f"Total Products: {len(my_bakery)}")
print(f"Total Quantity: {sum(my_bakery.values())}")
