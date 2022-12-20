def gen_s(range_str):
    start, end = [int(x) for x in range_str.split(",")]
    return set(range(start, end + 1))


n = int(input())
lenght_of_interseptions = 0
longest_interseption_sequence = []
for i in range(n):  # 0,3-1,2
    my_range = input().split('-')
    set1 = gen_s(my_range[0])
    set2 = gen_s(my_range[1])
    set_result = set1.intersection(set2)
    if len(set_result) > lenght_of_interseptions:
        lenght_of_interseptions = len(set_result)
        longest_interseption_sequence = set_result


print(f"Longest intersection is [{', '.join([str(x) for x in longest_interseption_sequence])}] with length {lenght_of_interseptions}")


