class Contact:
    def __init__(self, name: str, phone: int):
        self.name = name
        self.phone = phone

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        is_digit_in_name = any([True for char in value if char.isdigit()])
        if is_digit_in_name:
            print("Need only letters in name")
        else:
            self.__name = value

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, value):
        is_letter_in_phone = any([True for digit in value if digit.isletter()])
        if is_letter_in_phone:
            print("Phone number must be only with digits")
        else:
            self.__phone = value


class MobilePhone:
    def __init__(self, manifacturer: str, make_year: int, model: str, contacts: dict):
        self.manifacturer = manifacturer
        self.make_year = make_year
        self.model = model
        self.contacts = {}

    def create_contact(self, name: str, phone: int):
        tmp_contact = Contact(name, phone)
        return tmp_contact

    def add_contact(self, name: str, phone: int):
        tmp_contact = self.create_contact(name, phone)
        self.contacts.setdefault(tmp_contact.name, tmp_contact.phone)

