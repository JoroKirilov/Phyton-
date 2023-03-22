import copy

#
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

# nested_list = [[1, 2, 3], [4, 5, 6]]
# new_nested_list = nested_list.copy()
# nested_list.append('v')
# nested_list[0][1] = 'a'
# print(id(nested_list))
# print(id(new_nested_list))
# print(id(new_nested_list[0]))
# print(id(nested_list[0]))
# print(nested_list)
# print(new_nested_list)


# def list_fabric(ls):
#     ls[1] = 23
#
#
# list1212 = {1: 3, 3: 3}
# list_fabric(list1212)
# print(list1212)
#
# import copy
#
# list1 = [[1, 2], 1, 2, 3, 4]
# list2 = copy.deepcopy(list1)
#
# list1.append("b")
# list1[0][0] = 'a'
# print(list1)
# print(list2)


set1 = {1, 2}
set1.add(34)

print(set1)
for ele in set1:
    print(ele)

print(dir(set1))


# def print_different(function):
#     def wrapper(a , b):
#         return function(a + 1, b + 1)
#     return wrapper
#
#
# @print_different
# def sum_nums(a, b):
#     return a + b
#
#
# print(sum_nums(1 , 1))


