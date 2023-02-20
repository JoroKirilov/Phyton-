from collections import deque

list1 = deque()
list1.append(5)
list1.append(6)
list1.append(7)
print(list(list1))

list1.popleft()
print(list1)
print(list1[0])