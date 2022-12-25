import re

data = input()
patter = r"[+]359[ -]\d[ -][0-9]{3}[ -][0-9]{4}\b"
matches = re.findall(patter, data)
print(matches)