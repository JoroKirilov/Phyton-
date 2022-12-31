def kwarg_lenght(**kwargs):
    print(len(kwargs))


duct = {
    'key': 1,
    'value': 2
}

kwarg_lenght(key=1, value=2, thirt=3)
