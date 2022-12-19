n = int(input())
list_names = set()
for _ in range(n):
    names = input()
    list_names.add(names)
print("\n".join(list_names))
