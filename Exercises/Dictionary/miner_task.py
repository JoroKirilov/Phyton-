line_counter = 0
dict_resources = {}
temp_list = []
while True:
    line = input()
    if line == 'stop':
        break
    temp_list.append(line)
for index in range(0, len(temp_list) - 1, 2):
    resource_value = int(temp_list[index + 1])
    dict_resources.setdefault(temp_list[index], 0)
    dict_resources[temp_list[index]] += resource_value

for key, value in dict_resources.items():
    print(f"{key} -> {value}")
