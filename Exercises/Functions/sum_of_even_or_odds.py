def sum_of_numbers(command: str, *args):
    parity = 0 if command == 'Even' else 1
    return sum([element for element in args if element % 2 == parity])


print(sum_of_numbers("Even", 1, 2, 3, 4, 5, 6, 7))