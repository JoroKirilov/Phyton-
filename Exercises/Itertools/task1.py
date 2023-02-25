import itertools

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

# letters= ["a", "b", "c"]
# digits = [1, 2, 3]
# names = ["Monica", "Veronica"]
# # combined = letters + digits + names
# combined = itertools.chain(letters,digits,names)
# for item in combined:
#     print(item)