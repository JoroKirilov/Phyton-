from collections import deque


my_deque = deque()


command = input()
while not command == "End":
    if command == "Paid":
        while my_deque:
            print(my_deque.popleft())
    else:
        my_deque.append(command)
    command = input()
print(f"{len(my_deque)} people remaining.")
