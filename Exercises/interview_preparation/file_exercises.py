import os

if os.path.isfile("file1.txt"):
    print("file is already exist")
else:
    with open("file1.txt", "w") as file:
        file.write("bomba")




