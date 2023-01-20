class Contact:
    def __init__(self, name: str, phone: str):
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
        is_letter_in_phone = any([True for digit in value if digit.isalpha()])
        if is_letter_in_phone:
            print("Phone number must be only with digits")
        else:
            self.__phone = value


class MobilePhone:
    def __init__(self, manifacturer: str, make_year: int, model: str):
        self.manifacturer = manifacturer
        self.make_year = make_year
        self.model = model
        self.contacts = {}
        self.call_counter = 0

    def create_contact(self, name: str, phone: str):
        tmp_contact = Contact(name, phone)
        return tmp_contact

    def add_contact(self, name: str, phone: str):
        tmp_contact = self.create_contact(name, phone)
        if name in self.contacts:
            print("Name exists in contacts.")
        else:
            self.contacts[tmp_contact.name] = tmp_contact.phone

    def edit_contact(self, name: str, new_phone: int):
        if name in self.contacts:
            self.contacts[name] = new_phone

    def dialing_contact(self, name):
        if name in self.contacts:
            self.call_counter += 1
            return f"Calling {name}..."
        else:
            return "Can't find contact with this name"


# create instance of class Phone
mobile1 = MobilePhone("LG", 2022, "G23")

# add contact
mobile1.add_contact("Ivan", '888960945')
print(mobile1.dialing_contact("Ivan"))

# add contact with existing name
mobile1.add_contact("Ivan", "39485")
mobile1.add_contact("Sonia", "5345345")
mobile1.dialing_contact("Sonia")

# get numbers of calls make with this phone
print(mobile1.call_counter)
