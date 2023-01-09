# Задача 2 - направете функция, която приема лист с ints и
# го връща подреден. Използвайте Insertion Sort
# алгоритъм.
# numbers = [8, 5, 2, 9, 5, 6, 3]
# expected_output = [2, 3, 5, 5, 6, 8, 9]

def insertion_sort(lst):
  for i in range(1, len(lst)):
    j = i-1
    key = lst[i]
    while j >= 0 and key < lst[j] :
        lst[j+1] = lst[j]
        j -= 1
    lst[j+1] = key
  return lst

numbers = [8, 5, 2, 9, 5, 6, 3]
print(insertion_sort(numbers))