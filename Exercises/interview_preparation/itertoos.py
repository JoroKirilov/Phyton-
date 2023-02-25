import itertools
lst = [12, 3, 1, 2, -6, 5, -8, 6]
target = 0
result_list = []
resutl = list(itertools.combinations(lst, 3))
print(resutl)
for el in resutl:
    if sum(el) == target and el not in result_list:
        result_list.append(el)

print(result_list)
