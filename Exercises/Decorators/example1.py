from datetime import datetime
from functools import singledispatch


def print_time_stats(func):
    def wrapper_func(*args):
        start_at = datetime.now()
        print(f"Start execution of {func.__name__} at {start_at}")
        func(*args)
        end_at = datetime.now()
        print(f"Finished execution of {func.__name__} at {end_at}")
        print(f"Execution of {func.__name__} took {(end_at - start_at).total_seconds()}")
    return wrapper_func


def bold_decorator(func):
    def wrapper_func(*args):
        func_result = func(*args)
        return f"<b>{func_result}</b>"
    return wrapper_func


def pre_tag_decorator(func):
    def wrapper_func(*args):
        func_result = func(*args)
        return f"<pre>{func_result}</pre>"
    return wrapper_func


@bold_decorator
@pre_tag_decorator
def capitalize_name(name: str):
    """print_name decorated function docstring"""
    return name.upper()


print(capitalize_name("test"))


@singledispatch
def printer(value):
    print(f"Other: {value}")


@printer.register(str)
def str_printer(value):
    print("Print string: ", value)


@printer.register(int)
def int_printer(value):
    print("Print integer: ", value)


@printer.register(dict)
def dict_printer(dictionary):
    for value in dictionary.values():
        print("Value of dict item is: ", value)


# printer({"name": "Pesho", "age": "uknown"})

@print_time_stats
def loop_in_a_billion():
    print("Start loop over 1B")
    for _ in range(1_000_000_001):
        continue
    print("End loop over 1B")


loop_in_a_billion()

def decorator_maker_with_arguments(decorator_arg1,decorator_arg2,decorator_arg3):
    def decorator(func):
        def wrapper(function_arg1,function_arg2,function_arg3):
            print(
                "The wrapper can access all the variables\n"
                "\t- from the decorator maker: {0} {1} {2}\n"
                "\t - from the function call: {3} {4} {5]\n"
                "and pass them to the decorated function".format(
                    decorator_arg1,
                    decorator_arg2,
                    decorator_arg3,
                    function_arg1,
                    function_arg2,
                    function_arg3,
                )
            )
            return func(function_arg1,function_arg2,function_arg3)
        return wrapper
    return decorator


pandas = "Pandas"


@decorator_maker_with_arguments(pandas, "Numpy", "Scikit-learn")
def decorated_function_with_arguments(function_args1,function_args2,function_args3):
    print(
        "This is the decorated funtion and it only knows about its arguments: {0}"
        "{1}"
        "{2}".format(function_args1, function_args2, function_args3)
    )
