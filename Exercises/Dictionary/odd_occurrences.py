words = [word for word in input().split()]
my_dict = {}
for word in words:
    my_dict.setdefault(word.lower(), 0)
    my_dict[word.lower()] += 1
for key, value in my_dict.items():
    if value % 2 != 0:
        print(key, end=" ")

