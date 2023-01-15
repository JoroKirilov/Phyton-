def who_see_sunset(arr: list):
    tmp_list = []
    left = 0
    for n in arr:
        if n > left:
            left = n
            tmp_list.append(n)
    return tmp_list



list1 = [0, 8, 0, 0, 10, 5, 7, 23, 54, 2, 100]

print(who_see_sunset(list1))

