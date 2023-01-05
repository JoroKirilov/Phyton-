# Use another function to find the minimum of y and z
def min_of_two(required=False):
    def decorator(func_ref):
        def wrapper(x, y, z):
            if required:
                return y if y < z else z
            else:
                return func_ref(x, y, z)
        return wrapper
    return decorator


@min_of_two(required=False)
def get_min_of_three_members(x, y, z):
    min_num1 = 0
    # finish the function by adding code that would return the minimum of x, y and z
    if x < y and x < y:
        return x
    elif y < x and y < z:
        return y
    else:
        return z

    # Do not use the builtin min()


print(get_min_of_three_members(1, 2, 3))
