text = input()
dict_count = {}
for char in text:
    if char == ' ':
        continue
    dict_count.setdefault(char, 0)
    dict_count[char] += 1

for key, value in dict_count.items():
    print(f'{key} -> {value}')
