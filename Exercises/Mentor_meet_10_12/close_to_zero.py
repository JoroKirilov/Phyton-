# Най-малката разлика - напишете функция, която получава два равни по дължина листа.
# Трябва да върнете двойката числа, чиято абсолютна разлика е най-близко до 0 под формата на лист.
# Примерен Input:
# arrayOne = [-1, 5, 10, 20, 28, 3]
# arrayTwo = [26, 134, 135, 15, 17]
# Очакван Output: [28, 26]

import sys


def find_zero_result(arr1, arr2):
    min_diff = sys.maxsize
    for i in range(len(arr1)):
        for y in range(len(arr2)):
            if min_diff > abs(arr1[i] - arr2[y]):
                min_diff = abs(arr1[i] - arr2[y])
                result = [arr1[i], arr2[y]]
    return result


arrayOne = [-1, 5, 10, 20, 28, 3]
arrayTwo = [26, 134, 135, 15, 17]
min_difference = find_zero_result(arrayOne, arrayTwo)
print(min_difference)
