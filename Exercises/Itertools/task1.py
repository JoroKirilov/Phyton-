import itertools
import operator

# counter = itertools.count(start=5, step=5)
#
# print(next(counter))
# print(next(counter))


# -------------zip two iterable with the longest length -------------
# -------------return list of tuple with (0, 100) , (0 , 200) .....


# data = [100, 200, 300, 400]
# daily_data = list(itertools.zip_longest(range(10), data))
# print(daily_data)
# -----------------------------------------------------------------------


# --------------turn on and turn off (cycle) --------------

# mode = itertools.cycle(["ON", "OFF"])
# print(next(mode))
# print(next(mode))
# print(next(mode))

# ---------------------------------------------------------
#
# repeat_time = itertools.repeat(2, times=3)
#
# print(next(repeat_time))
# print(next(repeat_time))
# print(next(repeat_time))


# -------------- toto 6/49 all combinations -----------

# list_toto = [i for i in range(1, 50)]
# print(list_toto)
# comb = itertools.permutations(list_toto, 6)
# for com in comb:
#     print(com)

# ----------------card game(only one combination)----------------------

#
# list_comb = [1, 2, 3]
# result = itertools.combinations(list_comb, 2)
# for i in result:
#     print(i)

# ---------------all combination(no repeat elements)-------------------------

# list_comb = [1,2,3]
# result = itertools.permutations(list_comb, 3)
# for i in result:
#     print(i)

# ----------security code (repeat values) ---------------------------------

# list_comb = [1, 2, 3, 0]
# result = itertools.product(list_comb, repeat=4)
# for i in result:
#     print(i)

# ----------------------chain----------------------------------

# letters = ["a", "b", "c"]
# digits = [1, 2, 3]
# names = ["Monica", "Veronica"]
# # combined = letters + digits + names
# combined = list(itertools.chain(letters,digits,names))
# print(combined)


# ------------------- islice ------------------------------------

# with open("text.txt", "r") as f:
#     result = list(itertools.islice(f, 3))
#
# for row in result:
#     print(row, end='')


# ---------------------compress----------------------------------

# lst = [1, 2, 3, 4, 5, 6]
# # lst_bool = [True, False, True, False, True, False]
#
# resutl = list(itertools.compress(lst, [True if el % 2 == 0 else False for el in lst]))
# print(resutl)

# ------------------------------ acuumulate --------------------------------------


# list1 = [el + 1 for el in range(10)]
# fabonaci = list(itertools.accumulate(list1))
# print(fabonaci)


# ------------------------------ groupby---------------------------------------------------
#
# data = [
#     {"name": "ivan",
#      "age": 22,
#      "city": "Plovdiv"},
#     {"name": "gosho",
#      "age": 32,
#      "city": "Plovdiv"},
#     {"name": "pesho",
#      "age": 43,
#      "city": "Sofia"},
#     {"name": "sofia",
#      "age": 23,
#      "city": "Varna"},
#     {"name": "ismail",
#      "age": 12,
#      "city": "Plovdiv"},
# ]
#
# dict1 = {}
# for el in data:
#     if not el["city"] in dict1:
#         dict1[el["city"]] = []
#     dict1[el["city"]].append(el)
#
# for key, value in dict1.items():
#     print(f"{key} : {len(value)}")


# ---------------the task with water barels -------------------
#
# from itertools import accumulate
# # def waterArea(heights):
# #     left_max = list(accumulate(heights, max))
# #     right_max = list(reversed(list(accumulate(reversed(heights), max))))
# #     depths = [min(lm, rm) for lm, rm in zip(left_max, right_max)]
# #     water = sum(depths) - sum(heights)
# #     return water
# #
# #
# # water_list4 = [0, 100, 0, 0, 10, 1, 1, 10, 1, 0, 1, 1, 0, 0]
# # print(waterArea(water_list4))
#
#
# list_test = [1, 5, 3, 4, 0]
# right_max = list(reversed(list(accumulate(reversed(list_test), max))))
# print(right_max)
# #
# # # [1, 5, 5, 5, 5]
# # # [5, 5, 3, 4, 0]
# # # [1, 5, 3, 4, 0]