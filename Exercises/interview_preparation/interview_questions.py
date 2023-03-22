# class A:
#     pass
#
# obj = A()
# obj.name = "georgi"
# print(obj.name)



# ------------------------------------------------

# list1 = [1, 43, 54, 75, 23, 54, 675]
# for i in range(len(list1) - 1):
#     for y in range(i + 1, len(list1)):
#         if list1[i] > list1[y]:
#             list1[i], list1[y] = list1[y], list1[i]
#
# print(list1)

# --------------------------------------------------

num = 9
# for x in range(num):
#     print(" "*(num-x-1)+'*'*(2*x+1))

sign = 0
for i in range(num):

    space = num - (i + 1)
    sign = 2*i + 1
    print(f"{space * ' '}{sign * '*'}")

for i in range(num - 1, 0, -1):
    space = num - i
    sign = i * 2
    print(f"{space * ' '}{sign * '*'}")


# ---------------------------------------------------
# import itertools
#
# n = 10
# list1 = [el + 1 for el in range(n)]
# fabonaci = list(itertools.accumulate(list1))
# print(fabonaci)
# n = 10
# list1 = [el for el in range(n + 1)]
# fibonaci = list(itertools.accumulate(list1 , ))
# print(fibonaci[-1])

# -------------------------------------------------------

# list1 = [1, 2, 3, 4, 5]
# target = 7
# for i in range(len(list1) - 2):
#     for y in range(i + 1, len(list1) - 1):
#         for x in range(y + 1, len(list1)):
#             if list1[i] + list1[y] + list1[x] is target:
#                 print(f"{list1[i]}, {list1[y]}, {list1[x]}")


# a = list(range(1, 11))
# print(a)













