my_bakery = {}
while True:
    delivery_info = input().split(": ")
    if delivery_info[0] == 'statistics':
        break
    stocks = delivery_info[0]
    quantity = delivery_info[1]
    if stocks in my_bakery:
        my_bakery[stocks] += int(quantity)
    else:
        my_bakery[stocks] = int(quantity)
print("Products in stock:")

for key, value in my_bakery.items():
    print(f"- {key}: {value}")

print(f"Total Products: {len(my_bakery)}")
print(f"Total Quantity: {sum(my_bakery.values())}")
