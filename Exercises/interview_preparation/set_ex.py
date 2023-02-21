# set is unordered

set1 = {1, 2, 3, 4}
set2 = {1, 2, 5, 6}

print(set1.difference(set2))  # difference
# set3 = set1 | set2
set3 = set1.union(set2)
print(set3)  # union

set_intersection = set1.intersection(set2)
print(set_intersection)

set_subset = {1, 2}.issubset({1, 2, 3})
print(set_subset)

set_symdifferense = set1.symmetric_difference(set2)
print(set_symdifferense)

print(dir(set1))

set1.add(23)
set1.add(12)
set1.add(44)
set1.add(14)
set1.discard(400)  # safety remove
sort_set = sorted(set1)
# set1.remove(500)
print(sort_set)