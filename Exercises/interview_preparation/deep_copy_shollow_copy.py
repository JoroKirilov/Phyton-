import copy

list1 = [1, 2, 3, 4]
list2 = list1.copy()
list3 = list1
list4 = copy.deepcopy(list1)
print(id(list1))
print(id(list2))
print(id(list3))
print(id(list4))

