# За домашно: Да се направи същото, но като сравнявате стойностите по индекси
# тоест arrayOne[0] - arrayTwo[0] дали е най-близката до 0 стойност
# после arrayOne[1] - arrayTwo[1]
# hint - използвайте zip()

import sys


def find_min_diff(arr, arr1):
    min_difference = sys.maxsize
    result_arr = []
    zip_result = zip(arr, arr1)
    elem, elem1 = zip(*zip_result)
    for i in range(len(elem)):
        if min_difference > abs(elem[i] - elem1[i]):
            min_difference = abs(elem[i] - elem1[i])
            result = [elem[i], elem1[i]]
    return result

arrayOne = [-1, 5, 10, 20, 28, 3]
arrayTwo = [26, 134, 135, 15, 17, 45, 54, 54]
print(find_min_diff(arrayOne, arrayTwo))
