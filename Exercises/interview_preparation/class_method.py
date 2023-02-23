# class Shop:
#     def __init__(self, name, type, capacity):
#         self.name = name
#         self.type = type
#         self.capacity = capacity
#
#     @classmethod
#     def small_shop(cls, name, type):
#         return cls(name, type, capacity=10)
#
#     def __str__(self):
#         return f"Shop '{self.name}' of type {self.type} is with {self.capacity} capacity"
#
#
# shop1 = Shop("Diana", "nonstop", 10)
# shop2 = Shop.small_shop("Iva", "nonstop")
#
# print(shop1)
# print(shop2)


# class Person:
#     min_age = 0
#     max_age = 100
#     def __init__(self, name, sex, status):
#         self.name = name
#         self.sex = sex
#         self.__status = self.validate_status(status)
#
#     @staticmethod
#     def validate_status(status):
#         if status > 10:
#             return 100
#         return 0
#
#     @classmethod
#     def validate_age(cls):
#         return True if cls.min_age > 16 else False
#
#     def __str__(self):
#         return f"{self.__status} is status for person"
#
# class Worker(Person):
#     min_age = 17
#     max_age = 55
#     def __init__(self, name, sex, status, role):
#         super().__init__(name, sex, status)
#         self.role = role
#
#     def __str__(self):
#         return f"{self.min_age}"
#
#
#
# w = Worker("ivan", "male", 11,  "worker")
# print(w.validate_age())
#
# p = Person("IVAN", "FEMALE", 11)
# print(p)


class Room:
    def __init__(self, number, capacity):
        self.number = number
        self.capacity = capacity
        self.guest = 0
        self.is_taken = False

    def take_room(self, people):
        if self.is_taken and self.capacity >= people:
            self.is_taken = True
            self.guest = people
            return
        return f"Room number {self.number} can not be taken"

    def free_room(self):
        if self.is_taken:
            self.is_taken = False
            self.guest = 0
        return f"Room number {self.number} not taken"


class Hotel:
    def __init__(self, name, stars):
        self.stars = stars
        self.name = name
        self.guest = 0
        self.rooms = []

    @classmethod
    def from_stars(cls, start_count):
        return cls(f"{start_count} stars Hotel", stars=5)

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        room = [r for r in self.rooms if r.number == room_number]
        return room[0].take_room(people)

    def free_room(self, room_number):

