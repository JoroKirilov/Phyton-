num = int(input())

for row in range(0, num + 1):
    print('*' * row)
for row in range(num - 1, 0, -1):
    print('*' * row)

