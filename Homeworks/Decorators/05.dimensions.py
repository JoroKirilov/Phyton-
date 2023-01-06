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

# list_dimension = []
# for row in range(6):
#     for col in range(6):
#         for elem in range(6):
#             if my_list[row][col][elem]:
#                 list_dimension.append(my_list[row][col][elem])
# print(list_dimension)





print(my_list[0][2][2])

