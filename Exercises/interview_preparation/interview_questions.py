# class A:
#     pass
#
# obj = A()
# obj.name = "georgi"
# print(obj.name)

# ------------------------------------------------

# list1 = [1, 43, 54, 75, 23, 54, 675]
# for i in range(len(list1)):
#     for y in range(i + 1, len(list1)):
#         if list1[i] > list1[y]:
#             list1[i], list1[y] = list1[y], list1[i]
#
# print(list1)

# --------------------------------------------------

# num = 9
# for x in range(num):
#     print(" "*(num-x-1)+'*'*(2*x+1))

# ---------------------------------------------------
import itertools

n = 10
list1 = [el + 1 for el in range(n)]
fabonaci = list(itertools.accumulate(list1))
print(fabonaci)
n = 10
list1 = [el for el in range(n + 1)]
fibonaci = list(itertools.accumulate(list1 , ))
print(fibonaci[-1])














