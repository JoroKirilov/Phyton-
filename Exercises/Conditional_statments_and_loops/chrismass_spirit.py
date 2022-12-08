quantity = int(input())
days = int(input())
ornament_set_price = 2
ornament_set_point = 5
skirt_price = 5
skirt_point = 3
garland_price = 3
garland_point = 10
light_price = 15
light_point = 17
price = 0
point = 0

for day in range(1, days + 1):
    if day % 11 == 0:
        quantity += 2
    if day % 2 == 0:
        price += ornament_set_price * quantity
        point += ornament_set_point
    if day % 3 == 0:
        price += (skirt_price + garland_price) * quantity
        point += skirt_point + garland_point
    if day % 5 == 0:
        price += light_price * quantity
        point += light_point
        if day % 3 == 0:
            point += 30
    if day % 10 == 0:
        point -= 20
        price += skirt_price + garland_price + light_price
        if day == days:
            point -= 30


print(f"Total cost: {price}")
print(f"Total spirit: {point}")





