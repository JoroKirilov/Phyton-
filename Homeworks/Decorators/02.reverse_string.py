# Add code that would return reversed string

def reverse_with_slice(text: str):
    return text[::-1]


def reverse_with_reverse_method(text : str):
    return reverse_string(text)


def reverse_string(string: str):

    temp_str = ''
    for index in range(len(string) - 1, -1, -1):
        temp_str += string[index]

    return temp_str


print(reverse_with_slice('vidvolP vitomokoL'))
print(reverse_string('vidvolP vitomokoL'))
print(reverse_with_reverse_method('vidvolP vitomokoL'))
