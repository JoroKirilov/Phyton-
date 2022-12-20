n = int(input())
my_set = set()
for _ in range(0, n):
    chemistry_element = input().split()
    for element in chemistry_element:
        my_set.add(element)

print("\n".join(my_set))
