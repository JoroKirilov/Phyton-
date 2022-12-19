n, m = input().split()
n = int(n)
m = int(m)
first_set = set()
second_set = set()

for i in range(0, n):
    num = input()
    first_set.add(num)
for i in range(0, m):
    num = input()
    second_set.add(num)

result_set = set()
result_set = first_set.intersection(second_set)
print("\n".join(result_set))