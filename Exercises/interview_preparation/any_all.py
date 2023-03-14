str1 = "aafsaasa"
# count = 0
# for char in str1:
#     if char.isupper():
#         count += 1
# if count > 0:
#     print('There is a upper char in str1')
# else:
#     print("ONLY LOWER CHAR")
# for char in str1:
#     print(char.upper(), end="")

# is_have_upper = all(True if char.islower() else False for char in str1)
# print(is_have_upper)
# is_have_upper = any(True if char.isupper() else False for char in str1)
# print(is_have_upper)



is_have_upper = [True if char.isupper() else False for char in str1]
print(is_have_upper)
is_any_upper_is_string = [True for char in str1 if char.isupper()]
print(is_any_upper_is_string)
