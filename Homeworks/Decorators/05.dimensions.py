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
    [1, 2, [3, 4, [6]]],
    [[], [], [3, 4, 5]]
]
new_list = []
for i in range(len(my_list)):
    for y in range(len(my_list[0])):
        for x in range(my_list[0][0]):
            if my_list[i][y][x]:
                new_list.append("-")
            else:
                new_list.append("")
print(new_list)



print(my_list[0][2][2])

my_list1 = [
    [1, 2],
    [3, 4],
    [5, 6],
]
