from collections import deque
people_on_deque = deque()
liters = int(input())
people = input()
while not people == "Start":
    people_on_deque.append(people)
    people = input()

command = input()
while not command == "End":
    if command.isdigit():
        name = people_on_deque.popleft()
        required_liters = int(command)
        if liters >= required_liters:
            liters -= required_liters
            print(f"{name} got water")
        else:
            print(f"{name} must wait")
    else:
        _, refil_liters = command.split()
        liters += int(refil_liters)
    command = input()
print(f"{liters} liters left")


