import re
data = input()

pattern = r"\d{2}([\./-])[A-Z][a-z]{2}\1\d{4}"
matches = re.finditer(pattern, data)
for match in matches:
    print(match.group())