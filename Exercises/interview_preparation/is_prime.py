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
#     a = 0
#     b = 1
#     result = 0
#     for i in range(1, n + 1):
#         result += a
#         a, b = b, a + b
#     return result
# print(fibonaci_num(9))

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

# ------------------
