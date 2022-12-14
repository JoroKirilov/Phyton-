list_name = []
counter = 0

while True:
    number_of_names = input("Enter number of names \n")
    if number_of_names.isdigit() and number_of_names != '0':
        break

while len(list_name) < int(number_of_names):
    name = input("Enter name \n")
    if name.isalpha():
        list_name.append(name)

list_name.sort()
print(list_name)
