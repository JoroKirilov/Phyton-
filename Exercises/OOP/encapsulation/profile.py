class Profile:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if 15 > len(value) > 5:
            self.__username = value
        else:
            raise ValueError("The username must be between 5 and 15 characters.")

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        is_valid_len = len(value) > 8
        is_upper_case_presented = any([True for char in value if char.isupper()])
        is_digit_presented = any([True for char in value if char.isdigit()])
        if is_digit_presented and is_valid_len and is_upper_case_presented:
            self.__password = value
        else:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

    def __str__(self):
        return fr'You have a profile with username: "{self.username}" and password: {"*"*len(self.__password)}'


p = Profile("Georgi", "909dAADSDA")
print(p.username)
print(p.password)
print(p)