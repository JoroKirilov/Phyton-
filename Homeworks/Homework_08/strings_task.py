def get_bigger_string(str1, str2):
    if len(str1) > len(str2):
        return str1, str2
    return str2, str1


str1 = "hellf"
str2 = "hello"

bigger_dict = {}
smaller_dict = {}
bigger_str, smaller_str = get_bigger_string(str1, str2)

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
        if not key in smaller_dict:
            count_dif += value
        elif bigger_dict[key] != smaller_dict[key]:
            count_dif += 1
    if count_dif <= 1:
        is_equal = True

elif len(str1) == len(str2):
    count_dif = 0
    for idx in range(len(str1)):
        if str1[idx] != str2[idx]:
            count_dif += 1
    if count_dif <= 1:
        is_equal = True
print(count_dif)

print(is_equal)
