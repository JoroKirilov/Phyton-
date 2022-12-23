# Write a function that receives two integer numbers. Calculate the factorial of each number.
# Divide the first result by the second and print the division formatted to the second decimal point.

def factoriel_of_number(number: int):
    factoriel = 1
    for i in range(1, number + 1):
        factoriel *= i
    return factoriel


def divide_two_numbers(num1: int, num2: int):
    return factoriel_of_number(num1) // factoriel_of_number(num2)


number1 = int(input())
number2 = int(input())
print(f"{divide_two_numbers(number1, number2):.2f}")


