text = input()
while True:
    try:
        num = int(input())
        break
    except ValueError as variable_error:
        print('must be digit:')
print(text * num)
