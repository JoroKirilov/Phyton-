def concatenate(*args):
    result = ''
    for word in args:
        result += word
        result += ' '
    return result



print(concatenate("Soft", "Uni", "is", "great"))

