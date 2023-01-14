dict1 = {}
dict1 = {"autor": {"iv0": 45}}
dict1["autor"].update({"gosho": 4})
dict1["autor"].update({"ivan" : 3})

for key, value in dict1.items():
    if "gosho" in value.keys():
        del dict1[key]["gosho"]
    print("true")
print(dict1)
