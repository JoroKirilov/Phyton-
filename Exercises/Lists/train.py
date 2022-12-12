number_of_wagons = int(input())
command = input()
train = [0 for _ in range(number_of_wagons)]

while command != 'End':
    command_list = command.split()
    if command_list[0] == "add":
        train[-1] += int(command_list[1])
    if command_list[0] == "insert":
        index = int(command_list[1])
        number_of_people = int(command_list[2])
        train[index] += number_of_people
    if command_list[0] == "leave":
        train[int(command_list[1])] -= int(command_list[2])
    command = input()

print(train)
