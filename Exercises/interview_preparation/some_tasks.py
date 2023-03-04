# food = input("What is your name:\n")
# print(f"{food}")
# is_good = "good" if food == "apple" else "no good"
# print(is_good)
import itertools
# import math
# import operator
# from functools import reduce
# from itertools import accumulate
#
# n = 3
# print(math.factorial(n))
# result = accumulate(range(1, n + 1), operator.mul)
# print(list(result)[-1])
#
# result1 = 1
# for i in range(1, n + 1):
#     result1 = i * result1
# print(result1)
#
# result_factoriel = reduce(operator.mul, range(1, n + 1))
# print(result_factoriel)
#
#
# def add_list(arr):
#     tmp_list = arr.copy()
#     tmp_list.append([1, 2, 3, 4, 5, 6])
#     return tmp_list
#
# list_of_numbers = [1, 2, 3, 4, 5, 6]
#
# lis = add_list(list_of_numbers)
# print(list_of_numbers)
# print(lis)

# def change_name():
#     global name
#     name = "Ivan"
#
# def new_name():
#     global name
#     name = "dragan"
#
#
# name = ""
# change_name()
# new_name()
# print(name)
#
# def koko(list_1):
#     list_1["one"] = 1
#
#
# a = {
#     "five": 5,
#     "six": 6
#      }
# koko(a)
# print(a)

# str1 = "text.py"
# print(dir(str1))
# idx = str1.rfind(",")
# print(str1[idx:])

list_with_files = ["core.py", "lore.py", "ivan.txt", "koiepoponai.txt"]
for el in list_with_files:
    if el.endswith(".py"):
        print(el)

str2 = "gkirilov1987@abv.bg"
str2 = str2.partition("@")
print(str2[0])
