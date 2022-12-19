POWER = 2


def power(x, y=POWER, o=10, /, name="Ivan"):
    result = 1
    while y > 0:
        result *= x
        y -= 1
    return result + o, name


print(power(3, name="print"))
