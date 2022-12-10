word = input()
word1 = input()
temp_string = ""
compare_string = word

for iteration in range(len(word)):
    for idx in range(iteration + 1):
        temp_string += word1[idx]
    for idx_1 in range(iteration + 1, len(word)):
        temp_string += word[idx_1]
    if not compare_string == temp_string:
        print(temp_string)
    compare_string = temp_string
    temp_string = ""
