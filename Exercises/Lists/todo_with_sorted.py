note = input()
my_list = {}
while note != "End":
    data = note.split('-')
    importance = int(data[0])
    task = data[1]
    my_list[task] = importance
    note = input()

my_dict = sorted(my_list.items(), key=lambda x: x[1])

for key,value in my_dict:
    print(value, end="")
    print(key)