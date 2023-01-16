def available_to_see_sunset(input_list):
    sunset_available = []
    if len(input_list) > 0:
        max_height = max(input_list)
        max_id = input_list.index(max_height)
        sunset_available.append(max_height)
        sunset_available = available_to_see_sunset(input_list[:max_id]) + sunset_available
    return sunset_available



input2 = [2, 3, 4, 5, 9, 6, 7, 10, 8]
input3 = []

print(available_to_see_sunset(input2))
print(available_to_see_sunset(input3))