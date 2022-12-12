note = input()
my_list = [0 for _ in range(10)]
while note != "End":
    data = note.split('-')
    importance = int(data[0])
    task = data[1]
    my_list.insert(importance, task)
    note = input()
result = []
result = [element for element in my_list if element != 0]

print(result)