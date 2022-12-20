text = input()

my_list = []
for char in text:
    my_list.append(char)

my_tuple = tuple(sorted(my_list))
my_set = set(my_tuple)

for char in sorted(my_set):
    print(f"{char}: {my_tuple.count(char)} time/s")

