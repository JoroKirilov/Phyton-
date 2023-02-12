list1 = [-1, 2, 3, -43, 23]
list2 = [el * -1 if el < 0 else el for el in list1]
print(list2)
a = 4 if len(list2) > 2 else 7
print(a)

a = [1, 2, 3, 4, 5, 6]
result = ["even" if num % 2 == 0 else "odd" for num in a]
print(result)