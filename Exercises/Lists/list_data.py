my_list = [14, 34.5, "Plovdiv", 34, 'A', 54 ]
new_list = []
for el in my_list:
    if isinstance(el, int):
        new_list.append(el)

print(*new_list)