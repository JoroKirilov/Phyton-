divider = int(input())
boundary = int(input())
max_number = 0
for number in range(1, boundary + 1):
    if number % divider == 0:
        max_number = number
print(max_number)
