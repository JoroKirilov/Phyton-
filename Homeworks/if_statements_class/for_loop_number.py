
for number in range(2000, 3501):
    if number % 7 == 0 and number % 5 != 0:
        print(f"{number},", end="")
