# Write a program that receives a sequence of numbers (integers) separated by a single space.
# It should print `a list of only the even numbers. Use filter().

# def print_only_even(arr_of_numbers):
#     for numbers in arr_of_numbers:
#         print()


numbers = [int(number) for number in input().split(" ")]
even_number = filter(lambda x: x % 2 == 0, numbers)
print(list(even_number))
