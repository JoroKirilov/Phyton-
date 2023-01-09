# Задача 1 - направете функция, която приема лист с ints. и
# го връща подреден. Използвайте Bubble Sort алгоритъм.
# numbers = [8, 5, 2, 9, 5, 6, 3]
# expected_output = [2, 3, 5, 5, 6, 8, 9]

def bubble_sort(arr):
    for i in range(len(arr)):
        for y in range(i+1, len(arr)):
            if arr[i] > arr[y]:
                arr[i], arr[y] = arr[y], arr[i]
    return arr


numbers = [8, 5, 2, 9, 5, 6, 3]
print(bubble_sort(numbers))
