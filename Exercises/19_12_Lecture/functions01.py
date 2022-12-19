def print_data(name: str, ages: int, courses=None, callback=None):
    """
    Print function will be used to print the data.
    :param name: human name
    :param ages: human ages
    :return: NONE
    """
    print(f"Human is {name}, ages:{ages}.", end="" if courses is not None else "\n")
    if courses:
        print(f"Human {name} graduate at {courses}.")
    print(name)
    print(ages)
    print(courses)
    if callback is not None:
        callback(name, ages)


def callback_func_example(name, ages):
    print(f"{name} is {ages} years old")

def store_names(name: str, names=[]):
    if len(names):
        names.append(name)
    return names


if __name__ == "__main__":
    n = "GEORGI"
    m = 34
    print_data(n, m, courses="Python", callback=callback_func_example)

print(print_data.__doc__)

    # store_names("Joro")
    # store_names("Ivan")



