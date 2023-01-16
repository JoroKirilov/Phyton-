from Inheritance.homework_steering_wheel.library.library import Library
from Inheritance.homework_steering_wheel.library.registration import Registration
from Inheritance.homework_steering_wheel.library.user import User

user1 = User(12, 'Peter')
user2 = User(14, "Ivan")
library = Library()
registration = Registration()
registration.add_user(user1, library)
registration.add_user(user2, library)
