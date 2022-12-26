import re
text = input()
pattern = r"\d+"
list_match = []
while text:
    match_number = re.findall(pattern, text)
    if match_number:
        list_match.extend(match_number)
    text = input()
print(*list_match, sep=' ')
