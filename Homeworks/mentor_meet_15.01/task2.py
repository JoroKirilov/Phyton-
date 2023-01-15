def sunset(arr: list):
    blocks_sunset = []
    max_block = max(arr)
    index_of_max_block = arr.index(max_block)
    blocks_sunset.append(arr[0])
    for idx in range(1, index_of_max_block + 1):
        if arr[idx] > max(arr[:idx]):
            blocks_sunset.append(arr[idx])

    return blocks_sunset


print(sunset([999990, 5, 2222, 7000, 7, 4000, 40]))

