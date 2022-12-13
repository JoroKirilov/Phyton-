nums = [int(el) for el in input().split()]
data = input()
my_list = list()
while not data == 'end':
    command, additionalData = data.split()
    if command != 'remove':
        _, fromIndex, _,countIndex = additionalData.sp
        command, removeIdx, fromIndex, _, countIndex = data.split()
        first_part = nums[:int(fromIndex)]
        exact_part = nums[int(fromIndex):(int(countIndex) + int(fromIndex))]
        last_part = nums[(int(countIndex) + int(fromIndex)):]
        if command == 'reverse':
            exact_part.reverse()
        else:
            exact_part.sort()
        my_list = first_part + exact_part + last_part
    else:
        toIndexToRemove = int(removeIdx)
        my_list = nums[toIndexToRemove:]

    data = input()

print(my_list)
