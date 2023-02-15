# ------------ decorator and function that don't get arguments -----------

# def get_volew_filter(function):
#     def wrapper():
#         letter = function()
#         return [let for let in letter if let in "acuoi"]
#     return wrapper
#
# @get_volew_filter
# def get_letter():
#     return ['a', 'b', 'c', 'd', 'e']
#
# print(get_letter())


# ----------- decorators that get arguments ---------------

# def repeat(n):
#     def decorator(fucntion):
#         def wrapper():
#             tmp_str = ''
#             for _ in range(n):
#                 tmp_str += fucntion()
#                 tmp_str += '\n'
#             return tmp_str
#         return wrapper
#     return decorator
#
# @repeat(10)
# def say_hi():
#     return 'Hello'
#
# print(say_hi())

# --------------------- function that get arguments -------------------------
# def even_number(function):
#     def wrapper(numbers):
#         res = [el for el in numbers if el % 2 == 0]
#         return res
#     return wrapper
#
# @even_number
# def get_numbers(numbers):
#     return numbers
#
# print(get_numbers([1, 2, 3, 4]))