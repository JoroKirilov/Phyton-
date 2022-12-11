def tripple_nums(items, target):
    result = list()

    for i in range(len(items) - 2):
        for j in range(i + 1, len(items) - 1):
            for k in range(j + 1, len(items)):
                if items[i] + items[j] + items[k] == target:
                    result.append(sorted([items[i], items[j], items[k]]))

    return result


lst = [12, 3, 1, 2, -6, 5, -8, 6]
target = 0

print(sorted(tripple_nums(lst, target)))