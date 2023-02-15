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