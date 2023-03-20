n = 4
for i in range(1, n + 1):
    space = n - i
    print(" " * space, end='')
    print("* " * i)

for i in range(n - 1 , 0, -1):
    space = n - i
    print(" " * space, end='')
    print("* " * i)
