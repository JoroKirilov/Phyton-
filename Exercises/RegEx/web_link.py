import re

input_text = input()
pattern = r"(?<=\s)w{3}\.[A-Za-z0-9-]+(\.[a-z]+)+(?=\s)"
while input_text:
    for el in re.finditer(pattern, input_text):
        print(el.group())
    input_text = input()
