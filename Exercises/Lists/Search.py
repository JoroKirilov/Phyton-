n = int(input())
key_word = input()
result_list = []
for i in range(n):
    current_string = input()
    result_list.append(current_string)
print(result_list)
for i in range(len(result_list)- 1, -1, -1):
    element = result_list[i]
    if key_word not in element:
        result_list.remove(element)
print(result_list)
