# def get_is_password_valid():
#     # Ask for user's password.
#     # Check user's password against the following conditions:
#     # At least 6 symbols, and maximum of 32 symbols.
#     # At least 1 upper case letter.
#     # At least 1 symbol.
#     # hint: use the re library.
#     pass

import re

pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{6,32}$"
password = input("Enter string to test: ")
result = re.findall(pattern, password)

if result:
    print("Valid password")
else:
    print("Password not valid")
