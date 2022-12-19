n = int(input())
list_cars = set()
for _ in range(n):
    action, car_number = input().split(', ')
    if action == "IN":
        list_cars.add(car_number)
    elif action == "OUT":
        list_cars.discard(car_number)
if list_cars:
    print('\n'.join(list_cars))
else:
    print("Parking Lot is Empty")