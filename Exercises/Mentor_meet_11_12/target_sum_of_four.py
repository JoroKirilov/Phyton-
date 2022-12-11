def target_sum(arr, target_sum):
    result = []
    for i in range(len(arr) - 3):
        for y in range(i + 1, len(arr) - 2):
            for z in range(y + 1, len(arr) - 1):
                for t in range(z + 1, len(arr)):
                    if (arr[i] + arr[y] + arr[z] + arr[t]) == target_sum:
                        result.append(sorted([arr[i], arr[y], arr[z], arr[t]]))

    return result


my_list = [12, 3, 1, 2, -6, 5, -8, 6]
target = 0
print(target_sum(my_list, target))
