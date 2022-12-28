class NegativeInvalidNumber(Exception):
    pass


sum_numbers = 0
while True:
    try:
        numbers = int(input())
        if numbers < 0:
            raise NegativeInvalidNumber
    except NegativeInvalidNumber:
        print("Operation is allowed only with positive numbers")
        continue
    sum_numbers += numbers
    if numbers == 0:
        break
print(sum_numbers)