from collections import deque
my_list = []
first_print = []
while True:
    commands = input().split()
    if commands == ["end"]:
        for el in first_print:
            print("\n".join(el))
        print(f"{len(my_list)} people remaining.")
        break
    if commands == ["paid"]:
        for el in my_list:
            first_print.append(el)
        my_list.clear()
    if commands != ["end"] and commands != ["paid"]:
        my_list.append(commands)
