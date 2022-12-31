def even_odd(*args):
    command = args[-1]
    even_nums = []
    odd_nums = []
    for index in range(len(args) - 1):
        if args[index] % 2 == 0:
            even_nums.append(args[index])
        else:
            odd_nums.append(args[index])
    return even_nums if command == 'even' else odd_nums


