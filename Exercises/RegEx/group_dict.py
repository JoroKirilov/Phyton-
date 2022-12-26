import re
data = input()

pattern = r"(?P<day>\d{2})(?P<separator>[\./-])(?P<month>[A-Z][a-z]{2})(?P=separator)(?P<year>\d{4})"
matches = re.finditer(pattern, data)
for match in matches:
    print(f"Day: {match['day']}, Month: {match['month']}, Year: {match['year']}")