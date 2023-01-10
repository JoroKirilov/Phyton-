def get_bigger_string(str1, str2):
    if len(str1) > len(str2):
        return str1, str2
    return str2, str1


str1 = "hell0o"
str2 = "hello"

bigger_dict = {}
smaller_dict = {}
bigger_str, smaller_str = get_bigger_string(str1, str2)
# make two dictionaries with key "chars of strings" and value "numbers of chars"
for element in bigger_str:
    bigger_dict.setdefault(element, 0)
    bigger_dict[element] += 1
for element in smaller_str:
    smaller_dict.setdefault(element, 0)
    smaller_dict[element] += 1

count_dif = 0
is_equal = False


result_dif = len(str1) - len(str2)

if abs(result_dif) == 1:
    for key, value in bigger_dict.items():
        # check if some key is missing in other dict we increase count diff with values of that key
        if not key in smaller_dict:
            count_dif += value
        # check if keys in not with the same value and increase count diff with 1
        elif bigger_dict[key] != smaller_dict[key]:
            count_dif += 1
    # if we have only one difference we can say that we can fix that two strings
    if count_dif <= 1:
        is_equal = True
# if strings is with equal length , we check element by element and if is only difference we return TRUE
elif len(str1) == len(str2):
    count_dif = 0
    for idx in range(len(str1)):
        if str1[idx] != str2[idx]:
            count_dif += 1
    if count_dif <= 1:
        is_equal = True


print(is_equal)
