def sum_num(num):
    return num + 45

numbers = [int(num) for num in input().split()]
numbers1 = [sum_num(num) for num in numbers if int(num) > 0]
print(numbers1)

a = 5 if len(numbers) > 5 else 66
print(a)

