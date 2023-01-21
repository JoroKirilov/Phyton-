# Напишете функция, която приема лист от стрингове и групира в друг лист анаграмите.
# Примерен вход: ['yo', 'act', 'flop', 'tac', 'foo', 'cat', 'oy', 'olfp']
# Примерен изход: [['yo', 'oy'], ['flop', 'olfp'], '[act', 'tac', 'cat'], ['foo']]


my_list = ['yo', 'act', 'flop', 'tac', 'foo', 'cat', 'oy', 'olfp']
dict1 = {}
dict2 = {}
list_result = []

for i in range(len(my_list)):
    for y in range(i + 1, len(my_list)):
        is_false = any([False for char in my_list[]])

