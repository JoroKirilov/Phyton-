from helper.fibonachi_helper import dict_mapper
while True:
    data = input().split()
    if data[0] == 'Stop':
        break
    if data[0] == 'Create':
        result = dict_mapper[data[0]](int(data[2]))
        tmp_num = int(data[2])
        print(*result, sep=' ')
    elif data[0] == 'Locate':
        result = dict_mapper[data[0]](int(data[1]), tmp_num)
        print(f"The number {data[1]} is at index {result}")
