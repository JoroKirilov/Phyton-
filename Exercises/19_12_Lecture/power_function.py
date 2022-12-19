def power(x, y=2):
    result = 1
    while y > 0:
        result *= x
        y -= 1
    return result



print(power(3))
