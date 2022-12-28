text = input()
while True:
    try:
        num = int(input())
        break
    except ValueError as variable_error:
        print('must be digit:')
print(text * num)


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0][-3])