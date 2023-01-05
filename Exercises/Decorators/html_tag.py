def tags(tag_name):
    def decorator(func):
        def wrapper(*args):
            func_result = func(*args)
            return f"<{tag_name}>{func_result}</{tag_name}>"
        return wrapper
    return decorator


@tags('div')
def join_string(*args):
    return "".join(args)


print(join_string("Hello," " you!"))
