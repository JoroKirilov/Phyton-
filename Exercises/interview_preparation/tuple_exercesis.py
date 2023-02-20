# tuple1 = (1, 2, 2.5, 5, 1, 4, 2.5, 5, 6, 6, 6, 8)
# tmp_dict = {}
# for nums in tuple1:
#     tmp_dict[nums] = tuple1.count(nums)
# print(tmp_dict)
#
# dict1 = {}
# dict1[1] = 4
# dict1[1] = 5
# dict1[1.1] = 4
# print(dict1)

dict1 = {}
list_names = ["tete", "tete", "goso", "tete"]
list_grades = [1, 2, 3, 45]
for idx in range(len(list_names)):
    if not list_names[idx] in dict1:
        dict1[list_names[idx]] = []
    dict1[list_names[idx]].append(list_grades[idx])
print(dict1)

result = 0
for key, value in dict1.items():
    for value1 in value:
        result += value1
    dict1[key] = result
    result = 0


print(dict1)

