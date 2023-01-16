from Inheritance.homework_steering_wheel.library.library import Library
from Inheritance.homework_steering_wheel.library.registration import Registration
from Inheritance.homework_steering_wheel.library.user import User

user1 = User(12, 'Peter')
user2 = User(14, "Ivan")
library = Library()
registration = Registration()
registration.add_user(user1, library)
registration.add_user(user2, library)
registration.change_username(12, "Gopeto", library)
registration.change_username(14, "Ivo", library)

[print(f'{user_rec.user_id}, {user_rec.username}, {user_rec.books_rent}') for user_rec in library.user_record]

library.books_available.update({'J.K.Rowling': ['The Chamber of Secrets',
                                                'The Prisoner of Azkaban',
                                                'The Goblet of Fire',
                                                'The Order of the Phoenix',
                                                'The Half-Blood Prince',
                                                'The Deathly Hallows']})

library.get_book('J.K.Rowling', 'The Deathly Hallows', 17, user1)
print(library.books_available)
