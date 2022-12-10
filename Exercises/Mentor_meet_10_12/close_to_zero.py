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
