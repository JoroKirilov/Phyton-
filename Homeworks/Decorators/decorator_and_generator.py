# Define looking_glass context manager that should print out text reversed
# version while Context manager is active with looking_glass():

# IF LOOKING_GLASS IS ACTIVE
# OUTPUT : ohcniM ,ohsoG ,ohseP
# ELSE
# OUTPUT : Pesho, Gosho, Mincho


def looking_glass(is_active=False):
    def decorator(func_ref):
        def wrapper(*args):
            if is_active:
                tmp_list = [name[::-1] for name in args]
                print(", ".join(tmp_list))
            else:
                return func_ref(*args)
        return wrapper
    return decorator


@looking_glass(is_active=True)
def print_name(*args):
    output_str = ", ".join(args)
    print(output_str)


print_name("Pesho", "Gosho", "Mincho")