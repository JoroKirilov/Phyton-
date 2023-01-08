def to_upper(func_ref):
    def wrapper():
        result = func_ref()
        return result.upper()
    return wrapper


@to_upper
def say_hi():
    return "Say Hi"


@to_upper
def say_zdrasti():
    return "Zdravei"


print(say_hi())
print(say_zdrasti())