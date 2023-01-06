# 2. Write decorator login_required that would be used to check if a user is logged, and if not,
# it should print out "Login required", and if user is logged, the decorated function should print
# "Welcome"
login_data = {
    "Georgi87": "LokoPlovdiv",
    "IvanIvanov": "svoshtov",
    "Pesho91": "sexbog91"
}


def valid_login_data(username, password, data=login_data):
    if username in data:
        if data[username] == password:
            return True
    else:
        return False


def login_required(args):
    pass


@login_required
def login():
    input("Enter your user and pass")
    username = "Georgi87"
    password = "LokoPlovdiv"
    is_registred = valid_login_data(username, password)
    
