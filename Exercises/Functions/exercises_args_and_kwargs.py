# print(operate("+", 1, 2, 3))

def operate(operator: str, *args):
    result = 0
    if operator == "*" or operator == "/":
        result = 1

    for numbers in args:
        numbers = int(numbers)
        if operator == '+':
            result += numbers
        elif operator == '-':
            result -= numbers
        elif operator == '*':
            result *= numbers
        else:
            result /= numbers
    return result


print(operate("+", 1, 2, 3))
