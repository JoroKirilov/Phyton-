# 5) Напишете функция, която получава лист и чило. Трябва да пренаредите листа, като всички числа,
# които са равни на подаденото към функцията трябва да отидат най-отзад в листа.
# array = [2, 1, 2, 2, 2, 3, 4, 2]
# to_move = 2
# очакван output = [4, 3, 1, 2, 2, 2, 2, 2]

def some_sort(arr, number):
    temp_arr = []
    for element in arr:
        if element == number:
            temp_arr.append(element)
    for element in arr:
        if element != number:
            temp_arr.append(element)
    temp_arr.reverse()
    print(temp_arr)


my_array = [2, 1, 2, 2, 2, 3, 4, 2]
to_move = 1
some_sort(my_array, to_move)