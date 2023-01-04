def test1(func):
    def wrapper(*args):
        return func(*args) * 10
    return wrapper


@test1
def sum_num(*args):
    result = 0
    for arg in args:
        result += arg
    return result


print(sum_num(1, 2, 4, 5))