def sum_nums(a, b):
    return a + b


def sub_nums(a, b):
    return a - b


def multi_nums(a, b):
    return a * b


def divide_nums(a, b):
    result = 0
    while True:
        try:
            return a / b
        except ZeroDivisionError:
            print("Can't divide to zero!")
            b = int(input('Please enter another divider:'))
            print('\n')


def pow_nums(a, b):
    return a ** b


dict_operator = {
    '+': sum_nums,
    '-': sub_nums,
    '*': multi_nums,
    '/': divide_nums,
    '^': pow_nums
}
