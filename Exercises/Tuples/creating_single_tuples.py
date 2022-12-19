def sum_names(name1, name2):
    return name1 + name2, "Qko"


names = {"One": 1, "Two": 2}
print(type(names))

a = (names, )
print(type(a))
print(a)

result = sum_names(5, 6)
print(result)
