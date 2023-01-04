def type_check(type1):
    def decorator(func):
        def wrapper(num):
            if isinstance(num, type1):
                return func(num)
            else:
                return "Bad type"
        return wrapper
    return decorator


@type_check(int)
def times2(num):
    return num*2


print(times2(2))
print(times2('Not A Number'))
