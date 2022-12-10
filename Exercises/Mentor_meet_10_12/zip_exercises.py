number = [1, 3, 4, 5]
my_strings = ["one", "three", "four", "five"]
my_str = ("one", "three")

result = zip(number, my_strings, my_str)
my_set = set(result)
print(my_set)
