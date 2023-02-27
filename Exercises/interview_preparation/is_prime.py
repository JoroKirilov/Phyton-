# def check_is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True
#
#
# print(check_is_prime(10))

# ------------ fibonaci -----------------------

# def fibonaci_num(n):
#     fib_list = [0, 1]
#     for num in range(n - 1):
#         num1 = fib_list[-1]
#         num2 = fib_list[-2]
#         sum = num1 + num2
#         fib_list.append(sum)
#     return fib_list
#
# print(fibonaci_num(10))





# ---------- factoriel --------------
# import math
#
#
# def factoriel_num(n):
#     return(math.factorial(n))
#
# print(factoriel_num(5))


# ---------- square root -------------
# import math
#
# number =2.0
# print(number**0.5)
# print(math.sqrt(2))

# ------------ leap year ----------------
# year = 2032
# if year % 400 == 0 or year % 100 != 0 and year % 4 == 0:
#     print("year is leap")
# else:
#     print("not leap year")


# -------------- multiplication table ===========

# for num in range(0, 11):
#     print(f"{num} * 10 = {num * 10}")

# ----------------- swap to variables --------------
# a = 5
# b = 10
# a, b = b, a
# print(a)

# ------------------ if fibonaci num -----------------

#
# def is_fibonaci(n):
#     tmp_list = [0, 1]
#     while tmp_list[-1] <= n:
#         tmp_list.append(tmp_list[-1] + tmp_list[-2])
#     if n in tmp_list:
#         print(f"{n} is fibonaci number")
#     else:
#         print(f"{n} is not a fibonaci number")
#     return tmp_list
#
# num = 55
# list_fibonaci = is_fibonaci(num)
# print(list_fibonaci)

# --------------- cyrcle_area ----------------------

# def find_area_of_cyrcle(r):
#     PI = 3.14
#     return PI * r ** 2
#
# r = 2
# print(find_area_of_cyrcle(r))

# -------------- calendar -------------------------------
# import calendar
# year = calendar.calendar(2023)
# month = calendar.month(2023, 2)
# print(month)
# print(year)

# ------------------- factoriel --------------------------
# import math
#
# number = 5
# print(math.factorial(number))


# ------------------- all prime number in interval ---------

# def prime_num(n):
#     if n <= 1:
#         return False
#     for number in range(2, n):
#         if n % number == 0:
#             return False
#     else:
#         return True
#
# start = 10
# end = 20
# list_of_prime_numbers = []
# for number in range(start, end):
#     if prime_num(number):
#         list_of_prime_numbers.append(number)
#         print(f"{number} is prime")
#     else:
#         print(f"{number} in not a prime")