str1 = "aafsaasa"
# count = 0
# for char in str1:
#     if char.isupper():
#         count += 1
# if count > 0:
#     print('There is a upper char in str1')
# else:
#     print("ONLY LOWER CHAR")
# for char in str1:
#     print(char.upper(), end="")

# is_have_upper = all(True if char.islower() else False for char in str1)
# print(is_have_upper)
# is_have_upper = any(True if char.isupper() else False for char in str1)
# print(is_have_upper)



# is_have_upper = [True if char.isupper() else False for char in str1]
# print(is_have_upper)
# is_any_upper_is_string = [True for char in str1 if char.isupper()]
# print(is_any_upper_is_string)
#
# def push_button(current_on_off_butoon):
#     current_on_off_butoon[0] = not current_on_off_butoon[0]



# is_on = [False]
# push_button(is_on)
# print(is_on)
# push_button(is_on)
# print(is_on)
# push_button(is_on)
# print(is_on)


# sorting object task

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"{self.name} at age {self.age}"

p1 = Person("Ivan", 19)
p2 = Person("Georgi", 23)
p3 = Person("Ivo", 11)
list_with_object = [p1, p2, p3, Person("Zarko", 11)]
sort_object_result = sorted(list_with_object, key=lambda x: (x.age, x.name))
print(list(sort_object_result))