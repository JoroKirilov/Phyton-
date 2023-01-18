
def edit_contacts_phone(dict1, name, new_phone):
    if name in dict1:
        dict1[name] = new_phone






dict1 = {"gosho": 1, "pesho": 2}


edit_contacts_phone(dict1, "gosho", +45 )
print(dict1)