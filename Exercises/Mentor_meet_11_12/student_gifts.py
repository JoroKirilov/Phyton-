# примерен вход: [8, 4, 2, 1, 3, 6, 7, 9, 5]
# примерен изход: [4, 3, 2, 1, 2, 3, 4, 5, 1]

 # 8 < 4  |   8 4 2      4 2 1    2 1 3    1 3 6    3 6 7   6 7 9   7 9 5   |  5 < 9

my_list = [8, 4, 2, 1, 3, 6, 7, 9, 5]
gift_list = [0 for elements in range(len(my_list))]
left = 0
middle = 0
right = 0

if my_list[0] < my_list[1]:
    gift_list[0] = 1
else:
    gift_list[0] = 4
if my_list[-1] < my_list[-2]:
    gift_list[-1] = 1
else:
    gift_list[-1] = 4

for left in range(0, len(my_list) - 2):
    middle = left + 1
    right = middle + 1
    if my_list[middle] < my_list[left]:
        gift_list[middle] = gift_list[left] - 1
    else:
        gift_list[middle] = gift_list[left] + 1


print(gift_list)



