def even_number(function):
    def wrapper(numbers):
        return [num for num in numbers if num % 2 == 0]
    return wrapper


@even_number
def get_number(numbers):
    return numbers


print(get_number([1, 2, 3, 4, 5]))