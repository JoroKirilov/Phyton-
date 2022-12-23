# Write a function that checks if a given password is valid. Password validations are:
# •	It should be 6 - 10 (inclusive) characters long
# •	It should consist only of letters and digits
# •	It should have at least 2 digits
# If a password is valid, print "Password is valid".
# Otherwise, for every unfulfilled rule, print a message:
# •	"Password must be between 6 and 10 characters"
# •	"Password must consist only of letters and digits"
# •	"Password must have at least 2 digits"


def is_valid_password(pass_input: str):
    digits_count = 0
    is_valid = True
    if len(pass_input) < 6 or len(pass_input) > 10:
        print("Password must be between 6 and 10 characters")
        is_valid = False
    for char in pass_input:
        if char.isdigit():
            digits_count += 1
        if char.isdigit() or char.isalpha():
            continue
        else:
            print("Password must consist only of letters and digits")
            is_valid = False
    if digits_count < 2:
        print("Password must have at least 2 digits")
        is_valid = False

    if is_valid:
        print("Password is valid")


user_password = input()
is_valid_password(user_password)