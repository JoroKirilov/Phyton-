def num_action(j):
    j += 3


n = 4
num_action(n)  # int pass by value
print(n)


def add_char(string, char):
    string += char


str1 = "Hello"
add_char(str1, 'a')  # string pass by value again
print(str1)


def list_add(list11, n):
    list11.append(n)

list1 = [1, 2, 3]
list_add(list1, 5)  # list is pass by reference
print(list1)


def add_in_dict(dict1, key, value):
    dict1[key] = value

dict1 = {1: "hello"}
add_in_dict(dict1, 4, "four")  # dictionary is pass be reference
print(dict1)


def add_set_element(s, value):
    s.add(value)

set1 = {3, 32, 23, 3,114, 4, 125, 5, 2, 2}
add_set_element(set1, 10000)                        # set pass by reference
print(set1)
