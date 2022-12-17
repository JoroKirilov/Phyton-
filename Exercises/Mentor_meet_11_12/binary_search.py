# 4) Напишете функция, която приема сортиран лист и target Int.
# Използвайки binary search algorithm намерете дали дадената стойност се съдържа в листа и върнете индекса й.
# Ако я няма върнете -1.
# примерен вход:
# array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
# target = 33
# примерен изход:
# 3

def search_in_arr(arr, search_num):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == search_num:
            return mid
        elif arr[mid] > search_num:
            high = mid - 1
        elif arr[mid] < search_num:
            low = mid + 1
    return -1


array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
target = 33
print(len(array))
print(search_in_arr(array, target))
