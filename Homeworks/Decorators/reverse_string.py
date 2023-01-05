def reverse_with_slice(text: str):
    return text[::-1]


def reverse_with_reverse_method(text : str):
    return reverse_string(text)


def reverse_string(string):
    # Add code that would return reversed string
    temp_str = ''
    for index in range(len(string) - 1, -1, -1):
        temp_str += string[index]

    return temp_str


# Do not use slice notation or reverse()

print(reverse_with_slice('Lokomotiv'))
print(reverse_string('Lokomotiv'))
print(reverse_with_reverse_method('Lokomotiv'))
