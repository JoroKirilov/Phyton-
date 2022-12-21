def find_lowest_numbers(arr, num):
    tmp_list = []
    arr = sorted(arr)
    for idx in range(num):
        tmp_list.append(arr[idx])
    return tmp_list


input_list = [int(element) for element in input().split()]
num_of_eliminate = int(input())
lowest_numbers = find_lowest_numbers(input_list, num_of_eliminate)

for numbers in lowest_numbers:
    if numbers in input_list:
        input_list.remove(numbers)

print(*input_list, sep=", ")
