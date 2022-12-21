gifts = input().split()
while True:
    command = input().split()
    if command[0] == "No":
        break
    if len(command) == 2:
        action, item = command
        index = 0
    else:
        action, item, index = command
        index = int(index)

    if action == f"OutOfStock":
            gifts = [None if item == element else element for element in gifts]
    elif action == f"Required":
        if len(gifts) >= index:
            gifts.pop(index - 1)
            gifts.insert(index - 1, item)
    elif action == f"JustInCase":
        gifts.pop()
        gifts.append(item)

print(*gifts, sep=" ")

