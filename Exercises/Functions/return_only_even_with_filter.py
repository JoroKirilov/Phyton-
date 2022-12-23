def even_only(number: int):
    return True if number % 2 == 0 else False


list_of_numbers = [1, 2, 4, 5, 6, 2, 12, 13]
list_with_only_even_numbes = filter(even_only, list_of_numbers)
print(list(list_with_only_even_numbes))