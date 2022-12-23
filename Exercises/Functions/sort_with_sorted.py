# Write a program that receives a sequence of numbers (integers) separated by a single space.
# It should print a sorted list of numbers in ascending order.
# Use sorted().

def sort_list(numbers_to_sort):
    numbers_to_sort.sort()
    return numbers_to_sort


numbers = list(map(int, input().split(" ")))
sort_num = sort_list(numbers)
print(sort_num)