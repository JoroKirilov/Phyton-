# 2. Write decorator login_required that would be used to check if a user is logged, and if not,
# it should print out "Login required", and if user is logged, the decorated function should print
# "Welcome"
import time

login_data = {
    "Georgi87": "LokoPlovdiv",
    "IvanIvanov": "svoshtov",
    "Pesho91": "sexbog91",
    "1": "2"  # easy try program with this input
}


def valid_login_data(username, password, data=login_data):
    if username in data:
        if data[username] == password:
            return True
    else:
        return False


def login_required(func_ref):
    def wrapper():
        print("Login required")
        username = input("Enter your user name\n")
        password = input("Enter your password\n")
        print("Please wait...")
        time.sleep(4)
        if valid_login_data(username, password):
            return func_ref()
        else:
            return False

    return wrapper


@login_required
def login():
    print("Wellcome")
    return True


is_logged_in = login()
while True:
    if is_logged_in:
        break
    else:
        is_logged_in = login()
