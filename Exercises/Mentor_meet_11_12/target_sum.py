def tripple_nums(items, target):
    result = list()

    for i in range(len(items) - 2):
        for j in range(i + 1, len(items) - 1):
            for k in range(j + 1, len(items)):
                if items[i] + items[j] + items[k] == target:
                    result.append(sorted([items[i], items[j], items[k]]))

    return result


lst = [500, 400, 250, 250]
target = 1000

print(sorted(tripple_nums(lst, target)))