nums = [int(el) for el in input().split()]
data = input()
my_list = list()
while not data == 'end':
    command, _, fromIndex, _, countIndex = data.split()
    if command != 'remove':
        first_part = nums[:int(fromIndex)]
        exact_part = nums[int(fromIndex):(int(countIndex) + int(fromIndex))]
        last_part = nums[(int(countIndex) + int(fromIndex)):]
        if command == 'reverse':
            exact_part.reverse()
        else:
            exact_part.sort()

        for element in first_part:
            my_list.append(element)
        for element in exact_part:
            my_list.append(element)
        for element in last_part:
            my_list.append(element)
    else:
        toIndexToRemove = int(command[1])
        my_list = nums[toIndexToRemove:]

    data = input()

print(my_list)
