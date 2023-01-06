# 4. Write a Python function to create and print a list where the values are square of numbers
# between 1 and 30 (both included)


def square_number(func_ref):
    def wrapper(start, end):
        func_ref(start, end)
        print("")
        result = [number**2 for number in range(start, end + 1)]
        for number in result:
            print(number, end=' ')
    return wrapper


@square_number
def print_numbers(start, end):
    for number in range(start, end + 1):
        print(number, end=' ')


print_numbers(1, 30)