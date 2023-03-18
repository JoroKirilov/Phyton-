import math

print(dir(math))

list1 = [1, 2, 3, 2, [1, 2]]
print(dir(list1))
# list1.clear()
print(list1)
list1.reverse()
list1.reverse()
print(list1)
print(list1.count(1))
print(list1.index(2))
print(list1.index(2, 1, 4))
list1.insert(1, 34)
print(list1)
list1.pop(1)
print(list1)
list1.remove(2)
list1.remove(1)
print(list1)


# list1 = [1, 2, 3, 4, 5]
# target = 7
# for i in range(len(list1) - 2):
#     for y in range(i + 1, len(list1) - 1):
#         for x in range(y + 1, len(list1)):
#             if list1[i] + list1[y] + list1[x] is target:
#                 print(f"{list1[i]}, {list1[y]}, {list1[x]}")

