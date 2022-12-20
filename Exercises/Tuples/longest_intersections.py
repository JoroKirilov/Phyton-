def gen_seq(range_seq):
    start, end = [int(x) for x in range_seq.split(',')]
    return set(range(start, end + 1))

longest_set = set()

n = int(input())
for i in range(1, n + 1):
    data = input().split("-")
    set1 = gen_seq(data[0])
    set2 = gen_seq(data[1])
    set3 = set1.intersection(set2)
    if len(set3) > len(longest_set):
        longest_set = set3

print(f"Longest intersection is [{','.join([str(x) for x in longest_set])}] with length {len(longest_set)}")
