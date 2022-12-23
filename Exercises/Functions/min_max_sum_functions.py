# •	On the first line: "The minimum number is {minimum number}"
# •	On the second line: "The maximum number is {maximum number}"
# •	On the third line: "The sum number is: {sum of all numbers}"

def return_min_max_and_sum(numbers_list: list):
    min_value = min(numbers_list)
    max_value = max(numbers_list)
    sum_of_arr_elements = sum(numbers_list)
    return min_value, max_value, sum_of_arr_elements


numbers = [int(elements) for elements in input().split()]
min_value, max_value, sum_value = return_min_max_and_sum(numbers)
print(f"The minimum number is {min_value}")
print(f"The maximum number is {max_value}")
print(f"The sum number is: {sum_value}")