# n = int(input())
# set1 = set()
# for _ in range(n):
#     input_data = input().split(", ")
#     if input_data[0] == 'IN':
#         set1.add(input_data[1])
#     elif input_data[0] == 'OUT':
#         set1.discard(input_data[1])
#
# print("\n".join(set1))

list1 = [11, 8, 5, 6, 9, 2, 9, 7, 3, 4]
target = 11
for i in range(len(list1) - 1):
    for y in range(i+1, len(list1)):
        if list1[i] + list1[y] == target:
            print(f"{list1[i]} + {list1[y]} = {target}")
            list1.remove(list1[y])
            break

