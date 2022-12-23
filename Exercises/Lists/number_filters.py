def filter_numbers(list_of_numbers: list, command: str):
    tmp_list = []
    if command == 'even':
        tmp_list = list(filter(lambda x: x % 2 == 0, list_of_numbers))
    elif command == 'odd':
        tmp_list = list(filter(lambda x: x % 2 != 0, list_of_numbers))
    elif command == 'negative':
        tmp_list = list(filter(lambda x: x < 0, list_of_numbers))
    else:
        tmp_list = list(filter(lambda x: x >= 0, list_of_numbers))
    return tmp_list


n = int(input())
my_numbers_list = []
for _ in range(n):
    number = int(input())
    my_numbers_list.append(number)
command = input()

filtred_list = filter_numbers(my_numbers_list, command)
print(filtred_list)