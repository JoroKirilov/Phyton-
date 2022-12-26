import re
data = input()
numbers = []
pattern = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"
matches = re.finditer(pattern, data)
for match in matches:
    numbers.append(match.group())

print(*numbers, sep=' ')