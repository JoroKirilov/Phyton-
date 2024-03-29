# Напишете функция, която приема "специален" лист и връща сумата на този лист.
# "Специален" лист (никога не е празен) е лист, който съдържа цели числа или други
# "специални" листи. Сумата от "специалния" лист е сумата на елементите, които са умножени по нивото на тяхното nest-ване.
# Пример: [ ] този лист е с depth 1, ако има вложен лист [ [ ] ]: вътрешния ще е с depth 2
# [x, y] ще е равно на x + y
# [x, [y, z]] ще е равно на x + 2 * (y + z)
# [x, [y, [z]]] ще е равно на x + 2 * (y + 3z)
import math

# list1 = [1, [2, 3], 3, [2, 3, [1, 2]]]
# nested = 1
# sum = 0
# for idx in range(len(list1)):
#     if isinstance(list1[idx], list):
#         y = idx
#         while True:
#             nested += 1
#             y += 1
#             if not isinstance(list1[y], list):
#                 sum_of_nested_arr = 1 * nested
#                 nested = 1
#                 sum += sum_of_nested_arr
#                 break
#
#     else:
#         sum += list1[idx]
#
# print(sum)



# Фибоначи:
# Напишете функция, която да връща определено число от чилслата на фибоначи и неговата стойност. Функцията трябва да приема Int,
# който показва номерът на позицията на числото и трябва да връща стойността.
# Пример: Подаваме на функцията (3) и трябва да ни върне 1, защото третото число на Фибоначи е 1.
# Обяснение: Първите две числа на Фибоначи са 0 и 1. Всяко следващо число е сборът от предходните 2.

def fib_num(num):
    tmp_list = [0, 1]
    for el in range(num - 2):
        tmp_list.append(tmp_list[-1] + tmp_list[-2])
    return tmp_list[-1]

print(fib_num(1))


