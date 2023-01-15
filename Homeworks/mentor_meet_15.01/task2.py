# Примерен вход - [8,10,7,6,9,5,4,3,2]
# [2, 3, 4, 5, 9, 6, 7, 10, 8]
def sunset(arr: list):
    blocks_sunset = []
    max_block = max(arr)
    index_of_max_block = arr.index(max_block)
    blocks_sunset.append(arr[0])
    for idx in range(1, index_of_max_block):
        if arr[idx] > max(arr[:arr[idx]]):
            blocks_sunset.append(arr[idx])

    blocks_sunset.append(max_block)

    return blocks_sunset



print(sunset([2, 14, 6, 5, 11, 6, 7, 10, 20]))

