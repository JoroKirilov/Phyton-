def even_odd(command: str, *args):
    even_nums = []
    odd_nums = []
    for number in args:
        if number % 2 == 0:
            even_nums.append(number)
        else:
            odd_nums.append(number)
    return even_nums if command == 'even' else odd_nums


print(even_odd("even", 1, 2, 3, 4, 5, 6 ))