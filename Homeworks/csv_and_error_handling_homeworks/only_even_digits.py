def get_even_numbers(array):
    tmp_array = []
    for element in array:
        if element % 2 == 0:
            tmp_array.append(element)
    return tmp_array


my_list = [2, 3, 3, 6, 7, 9, 12]
print(get_even_numbers(my_list))
