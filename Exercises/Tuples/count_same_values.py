nums = (float(el) for el in input().split())
occ = {}
for num in nums:
    occ.setdefault(num, 0)
    occ[num] += 1

for key, value in occ.items():
    print(f"{key} - {value} times")
