import re

data = input()
patter = r"(\+359-2-\d{3}-\d{4}\b)|(\+359 \d [0-9]{3} [0-9]{4}\b)"
matches = re.finditer(patter, data)
# for p in matches:
#     print(p.group())
phones_list = [p.group() for p in matches]
print(', '.join(phones_list))