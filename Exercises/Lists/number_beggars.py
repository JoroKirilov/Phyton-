input_list = [int(el) for el in input().split(', ')]
beggars = int(input())
count_beggars_turn = 0
result_list = [0 for element in range(beggars)]
sum_of_elements = 0
for number_in_list in range(len(input_list)):
    if beggars > 0:
        result_list[count_beggars_turn] += input_list[number_in_list]
        count_beggars_turn += 1
        if count_beggars_turn == beggars:
            count_beggars_turn = 0

print(result_list)