# try:
#     file = open("some_text.txt", "w")
#     print(file.read())
# except IOError:
#     print("An I/O error")
# except:
#     print("An unknown error")
# else:
#     file.close()
import os
from pathlib import Path


print(Path(os.path.abspath(__file__)))
current_directory = Path(os.path.abspath(__file__)).parent
if os.path.exists("some_text.txt"):
    with open("some_text.txt" ,"r") as file_source:
        print(file_source.read())
else:
    print()
