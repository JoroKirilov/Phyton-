# 3. Write a function that would return if given int is within a certain range

def is_num_in_range(number, my_range="0 - 100"):
    start_range, _, end_range = my_range.split()
    start_range = int(start_range)
    end_range = int(end_range)
    return number if start_range <= number <= end_range else "Not in range"


print(is_num_in_range(0))
print(is_num_in_range(0, "4 - 40"))

