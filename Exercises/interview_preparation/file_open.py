# with open("file.txt", "w") as file:
#     file.write("Hello world")
list_str = []
with open("file.txt", "r") as file:
    for line in file.readlines():
        list_str.append(line[:-1])

print(list_str)

