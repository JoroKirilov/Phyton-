n = int(input())
sets_name = []
for _ in range(n):
    name = input()
    sets_name.append(name)

print('\n'.join(set(sets_name)))
