n = int(input())
count = 0
while count < n:
    str = input()
    counterChars = 0
    for char in str:
        if char != '_' and char != '.' and char != ',':
            counterChars += 1
    if counterChars == len(str):
        print(f"{str} is pure.")
    else:
        print(f"{str} is not pure!")
    n += 1
