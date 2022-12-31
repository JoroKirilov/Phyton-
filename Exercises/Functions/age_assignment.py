# print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
# Amy is 22 years old.
# Bill is 61 years old.
# Willy is 36 years old.


def age_assignment(*args, **kwargs):
    temp_dict = {}
    result_list_str = []
    for name in args:
        current_key = name[0]
        for key, value in kwargs.items():
            if current_key in key:
                temp_dict[name] = value
    return temp_dict

print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))