import os

def write_more():
    with open("file1.txt", "a") as f:
        f.write("more text")

with open("file1.txt", "w") as file:
    file.write("bomba")

write_more()

