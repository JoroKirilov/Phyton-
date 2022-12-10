single_string = input()
my_list = []
new_list = []
my_list = single_string.split(" ")
for elem in my_list:
    new_list.append(int(elem) * -1)
print(new_list)


