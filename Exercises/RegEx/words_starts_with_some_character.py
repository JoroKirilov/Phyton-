import re
text = input()
list_match = []
pattern = r"(^|\s?)_(?P<word>[A-Za-z0-9]+)\s?"
matches = re.finditer(pattern, text)
for match in matches:
    list_match.append(match['word'])

print(*list_match, sep=',')

