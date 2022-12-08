n = int(input())
count = 0
while count < n:
    string1 = input()
    counterChars = 0
    for char in string1:
        if char != '_' and char != '.' and char != ',':
            counterChars += 1
    if counterChars == len(string1):
        print(f"{string1} is pure.")
    else:
        print(f"{string1} is not pure!")
    n += 1
