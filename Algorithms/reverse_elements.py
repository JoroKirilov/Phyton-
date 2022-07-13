def reverse_elements(idx, elements):
    if idx == len(elements) // 2:
        return

    swap_index = len(elements) - 1 - idx
    elements[idx], elements[swap_index] = elements[swap_index], elements[idx]

    reverse_elements(idx + 1, elements)



elements = input().split()
reverse_elements(0, elements)
print(' '.join(elements))