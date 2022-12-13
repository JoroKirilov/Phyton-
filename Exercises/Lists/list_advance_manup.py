nums = [int(el) for el in input().split()]
command = input().split()
my_list = list()
while not command[0] == 'end':
    if command[0] != 'remove':
        fromIndex = int(command[2])
        countIndex = int(command[4])
        first_part = nums[:fromIndex]
        exact_part = nums[fromIndex:(countIndex + fromIndex)]
        last_part = nums[(countIndex + fromIndex):]
        if command[0] == 'reverse':
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

    command = input().split()

print(my_list)
