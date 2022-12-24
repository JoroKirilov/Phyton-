def get_info(**kwargs):
    output_data = f"This is {kwargs.get('name')} from {kwargs.get('town')} and he is {kwargs.get('age')} years old"
    return output_data

print(get_info(**{"name": "George", "town": "Sofia", "age": 20}))
