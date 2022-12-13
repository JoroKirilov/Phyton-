# 5) Напишете функция, която приема 2D лист.
# Функцията трябва да взима елементите на матрицата в спираловиден ред и да ги записва в лист.
# Накрая върнете листа.


def list_spiral(arr):
    row = 0
    temp_list = list()
    for _ in range(len(arr)):
        if row % 2 == 0:
            for idx in range(len(arr[row])):
                temp_list.append(arr[row][idx])
            row += 1

        else:
            for idx in range(len(arr[row]) - 1, -1, -1):
                temp_list.append(arr[row][idx])
            row += 1

    return temp_list


my_list = [
    [1, 2, 3, 4, 5],
    [12, 13, 14, 5, 5, 5, 5],
    [11, 16, 15, 6],
    [10, 9, 8, 7, 6, 6, 6, 6],
]

print(list_spiral(my_list))
