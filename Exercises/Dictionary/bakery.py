food_info = [element for element in input().split()]

my_dict = {}
for index in range(len(food_info)):
    if index % 2 == 0:
        my_dict[food_info[index]] = int(food_info[index + 1])
print(my_dict)