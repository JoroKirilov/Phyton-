# **5. Write a function that accepts multidimensional list and prints out list elements nested by
# their dimension:
# Example: [[1, 2, [3, 4, [6]]], [[], [], [3, 4, 5]]]
# 1, 2
#      3, 4
#          6
#
#
#          3, 4, 5
my_list = [
    [1,  2,  [3, 4, [6]]],
    [[], [],  [3, 4, 5]]
]

count_white_spaces = 0
white_space = " "
for row in range(len(my_list)):
    for col in range(len(my_list[0])):
        if isinstance(my_list[row][col], int):
            print(my_list[row][col], end=' ')
            count_white_spaces += 1
        elif isinstance(my_list[row][col], list):
            if my_list[row][col]:
                print("")
                print((count_white_spaces + 1) * white_space, end='')
                for elements in my_list[row][col]:
                    if isinstance(elements, int):
                        print(elements, end=' ')
                        count_white_spaces += 1
                    else:
                        count_white_spaces += 1
                        print("")
                        print((count_white_spaces + 1)*white_space, end='')
                        print("".join(map(str, elements)), end='')
            elif not my_list[row][col]:
                print("")











