def add_to_dict(**kwargs):
    tmp_dict = {}
    tmp_dict = kwargs
    tmp_dict["4"] = "Angel"
    return tmp_dict


my_dict = {'1': "Ivan", '2': 'Jordan', '3': 'Georgi'}
new_dict = add_to_dict(**my_dict)

print(new_dict)