import re
list_for_print = []
email_name = input()
pattern = r"(^|(?<=\s))[A-Za-z0-9]+[\.,_-]?[A-Za-z0-9]+@[A-Za-z]+\-?[A-Za-z]+(\.[A-Za-z]+)+($|(?=\s))"
match = re.finditer(pattern, email_name)
for m in match:
    list_for_print.append(m.group())

print(*list_for_print, sep='\n')