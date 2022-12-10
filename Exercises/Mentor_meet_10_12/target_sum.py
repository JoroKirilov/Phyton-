def find_target(arr, result):
    search_target = result
    for idx in range(len(arr)):
        search_target -= arr[idx]
        for idx1 in range(len(arr)):
            if idx != idx1:
                search_target -= arr[idx1]
                search2 = search_target
            for idx2 in range(len(arr)):
                if idx != idx1 and idx != idx2 and idx1 != idx2:
                    search_target -= arr[idx2]
                    if search_target == 0:
                        print("true")
                    search_target = search2



my_list = [12, 3, 1, 2, -6, 5, -8, 6]
target = 0
find_target(my_list, target)
