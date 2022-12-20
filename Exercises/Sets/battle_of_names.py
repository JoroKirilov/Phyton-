n = int(input())
odd_set = set()
even_set = set()
sum_of_char_values = 0
even_sum = 0
odd_sum = 0
for row in range(n):
    sum_of_char_values = sum([ord(element) for element in input()])
    sum_of_char_values //= row + 1
    if sum_of_char_values % 2 == 0:
        even_set.add(sum_of_char_values)
        even_sum += sum_of_char_values
    else:
        odd_set.add(sum_of_char_values)
        odd_sum += sum_of_char_values

if odd_sum > even_sum:
    result = odd_set.difference(even_set)
    #print(", ".join([str(x) for x in odd_set.difference(even_set)]))
elif odd_sum < even_sum:
    result = even_set.symmetric_difference(odd_set)
    #print(", ".join([str(x) for x in even_set.symmetric_difference(odd_set)]))
else:
    result = even_set.union(odd_set)
    #print(", ".join([str(x) for x in even_set.union(odd_set)]))

print(*result, sep=", ")


