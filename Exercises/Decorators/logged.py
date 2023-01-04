def logged(function):
    def wrapper(*args):
        arguments = "".join(str(args))
        text_result = f"you called {function.__name__}{arguments}"
        result = function(*args)
        return text_result + f"\nit returned {result}"
    return wrapper

@logged
def sum_func(a, b):
    return a + b

print(sum_func(1, 4))
