def store_result(func):
    def wrapper(*args):
        # Function 'add' was called. Result: 4
        func_result = func(*args)
        func_name = func.__name__
        with open('./result.txt', 'a') as file:
            file.write(f"Function '{func_name}' was called. Result: {func_result}\n")

    return wrapper


@store_result
def add(a, b):
    return a + b


print(add(6, 6))

