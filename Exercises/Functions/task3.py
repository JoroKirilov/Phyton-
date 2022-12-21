def calculator(command: str, number1: int, number2: int):
    result = 0
    if command == "multiply":
        result = number1 - number2
    if command == "divide":
        result = number1 // number2
    if command == "add":
        result = number1 + number2
    if command == "subtract":
        result = number1 - number2

    return result


type_action = input()
num1 = int(input())
num2 = int(input())

print(calculator(type_action, num1, num2))
