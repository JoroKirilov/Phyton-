def get_bigger_string(stt1, str2):
    if len(str1) > len(str2):
        return str1, str2
    return str1, str2


str1 = "000"
str2 = "as"
sorted_str1 = sorted(str1)
sorted_str2 = sorted(str2)
bigger_dict = {}
smaller_dict = {}
bigger_str, smaller_str = get_bigger_string(str1, str2)
for element in bigger_str:
    bigger_dict.setdefault(element, 0)
    bigger_dict[element] += 1
for element in smaller_str:
    smaller_dict.setdefault(element, 0)
    smaller_dict[element] += 1
print(bigger_dict)
print(smaller_dict)
count_dif = 0
is_equal = False


print(bigger_dict)
print(smaller_dict)
result = len(str1) - len(str2)
if abs(result) == 1:
    for key, value in bigger_dict.items():
        if not key in smaller_dict or bigger_dict[key] != smaller_dict[key]:
            count_dif += value
        print(count_dif)
    if count_dif <= 1:
        is_equal = True
elif len(str1) == len(str2):
    count_dif = 0
    for idx in range(len(str1)):
        if sorted_str1[idx] != sorted_str2[idx]:
            count_dif += 1
    if count_dif <= 1:
        is_equal = True
print(count_dif)

print(is_equal)
