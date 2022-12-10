def find_target(arr, result):
    search_target = result
    arr.sort()
    final_result = []
    count = 0
    for idx in range(len(arr)):
        search_target = result - arr[idx]
        for idx1 in range(len(arr)):
            if idx != idx1:
                search2 = search_target - arr[idx1]
                for idx2 in range(len(arr)):
                    if idx != idx1 and idx != idx2 and idx1 != idx2:
                        if search2 == arr[idx2]:
                            final_result.append({arr[idx], arr[idx1], arr[idx2]})
                            count += 1
    return final_result



my_list = [12, 3, 1, 2, -6, 5, -8, 6]
target = 0

print(find_target(my_list, target))
