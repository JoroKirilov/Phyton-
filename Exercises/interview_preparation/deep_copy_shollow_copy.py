import copy

list1 = [1, 2, 3, 4]
list2 = list1.copy()
list3 = list1
list4 = copy.deepcopy(list1)
list5 = [el + 1 if el > 2 else el for el in list1]
print(id(list1))
print(id(list2))
print(id(list3))
print(id(list4))
print(id(list5))

