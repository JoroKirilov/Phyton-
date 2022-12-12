numbers = [int(el) for el in input().split(", ")]
evens = [idx for idx in range(len(numbers)) if numbers[idx] % 2 == 0]
print(evens)