items = input().split('|')
budget = float(input())
profit = 0
all_profit = 0
profits = []
for item in items:
    item_type, item_price = item.split("->")
    item_price = float(item_price)
    if item_type == "Clothes" and item_price > 50:
        continue
    elif item_type == "Shoes" and item_price > 35:
        continue
    elif item_type == "Accessories" and item_price > 20.50:
        continue
    if budget >= item_price:
        budget -= item_price
        current_profit = (0.4 * item_price)
        profits.append(current_profit + item_price)
        all_profit += current_profit

for el in profits:
    print(f"{el:.2f} ", end="")
print()
print(f"Profits: {all_profit:.2f}")

if (sum(profits) + budget) >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")

