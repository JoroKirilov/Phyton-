# 3. Write a decorator that prints out "Mary Spring" whenever the decorated function is called.

def some_decorator(is_call=False):
    def decorator(func_ref):
        def wrapper():
            return "Mary Spring" if is_call else func_ref()
        return wrapper
    return decorator


@some_decorator(is_call=True)
def some_function():
    return "Mary Winter"


print(some_function())