# You will receive a single number. You should write a function that returns the sum of
# all even and all odd digits in a given number. The result should be returned as a single string in the format:
#
# "Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}"
# Print the result of the function on the console.

def sum_of_even_and_odd(string:str):
    sum_of_even = 0
    sum_of_ood = 0
    for char in string:
        number = int(char)
        if number % 2 == 0:
            sum_of_even += number
        else:
            sum_of_ood += number

    return sum_of_ood, sum_of_even


number_as_strings = input()
odd_sum, even_sum = sum_of_even_and_odd(number_as_strings)
print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")
