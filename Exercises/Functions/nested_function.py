# You will receive three integer numbers.
# Write functions named:
# •	sum_numbers() that returns the sum of the first two integers
# •	subtract() that returns the difference between the returned result of the first function and the third integer
# Wrap the two functions in a function named add_and_subtract() which will receive the three numbers as parameters.
# Print the result of the subtract() function on the console.

def sum_numbers(*args):
    return sum(args)


def subtract(num, num2, num3):
    return sum_numbers(num, num2) - num3


def add_and_substract(num1, num2, num3):
    return subtract(num1, num2, num3)


number1 = int(input())
number2 = int(input())
number3 = int(input())

print(add_and_substract(number1, number2, number3))
