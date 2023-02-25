import itertools

lst = [12, 3, 1, 2, -6, 5, -8, 6]
target = 0
result_list = []
resutl = list(itertools.combinations(lst, 3))

for el in resutl:
    if sum(el) == target:
        result_list.append(el)

print(result_list)
