import copy

#
# list1 = [1, 2, 3, 4]
# list2 = list1
#
#
# list4 = copy.deepcopy(list1)
# list3 = list1.copy()
# list1.append(6)
# print(list4)
# list5 = [el + 1 if el > 2 else el for el in list1]
# print(id(list1))
# print(id(list2))
# print(id(list3))
# print(id(list4))
# print(id(list5))

nested_list = [[1, 2, 3], [4, 5, 6]]
new_nested_list = nested_list.copy()
nested_list.append('v')
nested_list[0][1] = 'a'
print(id(new_nested_list[0]))
print(id(nested_list[0]))
print(nested_list)
print(new_nested_list)