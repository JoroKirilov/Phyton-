# n = 4
# for i in range(1, n + 1):
#     space = n - i
#     print(" " * space, end='')
#     print("* " * i)
#
# for i in range(n - 1 , 0, -1):
#     space = n - i
#     print(" " * space, end='')
#     print("* " * i)


# def check_is_prime(num):
#     if num == 1:
#         print("1 in not prime")
#     if num > 1:
#         for i in range(2, num):
#             if num % i == 0:
#                 print(f"{num} is not prime")
#                 return
#         print(f"{num} is prime")
#
# n = 3
# check_is_prime(n)


# def factoriel(num):
#     result = 1
#     list_of_factoriel = []
#     for i in range(1, num + 1):
#         result *= i
#         list_of_factoriel.append(result)
#
#     return list_of_factoriel

# from math import factorial
# n = 10
# result = factorial(n)
# print(result)

# from math import sqrt
#
# n = 4
#
# result = sqrt(n)
# print(result)


# def armstrong_num(num):
#     digits = len(str(num))
#     result = 0
#     for el in str(num):
#         result += int(el) ** digits
#
#     if result == num:
#         return f"{num} is armstrong"
#     return f"{num} is not armstrong"
#
# n = 1532
# print(armstrong_num(n))

# def is_leap_year(year):
#     if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
#         return "is leap"
#     return "not leap"
#
# print(is_leap_year(2005))

# def is_prime_num(num):
#     if num == 1:
#         return "is not prime"
#     elif num > 1:
#         for i in range(2, num):
#             if num % i == 0:
#                 return f"{num} is not prime"
#         return f"{num} is prime"
#
# n = 11
# print(is_prime_num(n))


# def mul_talbe():
#     for i in range(1, 11):
#         for y in range(1, 11):
#             print(f"{i} * {y} = {i * y}")
#
# mul_talbe()

# def is_fibonachi(num):
#     list1 = [0, 1]
#     for i in range(num):
#         list1.append(list1[-1] + list1[-2])
#         if list1[-1] >= num:
#             break
#     if num in list1:
#         return f"{num} is fibonachi"
#     return f"{num} is not fibonachi"
#
# print(is_fibonachi(1))

# from math import pi
# r = 4
# result = pi * r**2
# print(result)

# def is_prime(num):
#     if num > 1:
#         for i in range(2, num):
#             if num % i == 0:
#                 return False
#         return True
#
# def all_prime_number_in_range(start, end):
#     list_with_prime_num = []
#     for i in range(start, end + 1):
#         if is_prime(i):
#             list_with_prime_num.append(i)
#     return list_with_prime_num
#
# print(all_prime_number_in_range(10 ,20))

# favorite_prog = ["Python", "SQL", "GO"]
# result = " ".join(favorite_prog)
# print(result)

# str = "fafa ffa"
# a = str.title()
# print(a)

# def outer_function():
#     global num
#     num = 20
#
#     def inner_function():
#         global num
#         num = 30
#         print('num =', num)
#
#     inner_function()
#     print('num =', num)
#
#
# num = 10
# outer_function()
# print('num =', num)


# set1 = (1, 2, 3, 4, 5)
# set2 = set1[1:2:]
# for el in set2:
#     print(el)

# str1 = "fdfadfacdsaf"
# s = str1[8:0:-1]
# print(s)

# dict1 = {"a": 10, "b": 2, "c": 3}
# str1 = ""
# for i in dict1:
#     str1 = str1+str(dict1[i])+" "
#     str2 = str1[:-1]
# print(str2[::-1])


# def arg_train(age, year=4, *args, **kwargs):
#     print(args)
#     print(year)
#     print(f"ivan is {kwargs}")
#     for i in args:
#         print(i)
#
#
# arg_train(1, 2, 3, 4, "afa", 5, ivan=5)
#
# try:
#     x = 5 / 0
# except ZeroDivisionError:
#     print("Cannot divide by zero")
# else:
#     print("Division successful!")


class Laptops:
    def __init__(self, ram, gpu):
        self.ram = ram
        self.gpu = gpu

    @classmethod
    def gaming_laptop(cls):
        return cls(ram=32, gpu=1023)



l1 = Laptops.gaming_laptop()
print(l1.ram)