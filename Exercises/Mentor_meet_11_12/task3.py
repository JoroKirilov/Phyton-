# 3) Напишете функция, която приема лист с Int-ове. Функцията трябва да връща лист,
# който да съдържа резултатите на умножените числа (без настоящото).
# примерен вход = [5,1,4,2]
# примерен изход = [8,40,10,20]

def multi_arr(arr):
    tmp_list = []
    result = 1
    for idx in range(len(arr)):
        for idx1 in range(len(arr)):
            if idx != idx1:
                result *= arr[idx1]
        tmp_list.append(result)
        result = 1

    return tmp_list

list_int = [5, 1, 4, 2]
print(multi_arr(list_int))
