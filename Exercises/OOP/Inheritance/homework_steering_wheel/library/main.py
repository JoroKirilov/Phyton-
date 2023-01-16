from Inheritance.homework_steering_wheel.library.library import Library
from Inheritance.homework_steering_wheel.library.registration import Registration
from Inheritance.homework_steering_wheel.library.user import User

user1 = User(12, 'Peter')
user2 = User(14, "Ivan")
library = Library()
registration = Registration()
registration.add_user(user1, library)
registration.add_user(user2, library)

[print(f'{user_rec.user_id}, {user_rec.username}, {user_rec.books_rent}') for user_rec in library.user_record]

library.books_available.update({'J.K.Rowling': ['The Chamber of Secrets',
                                                'The Prisoner of Azkaban',
                                                'The Goblet of Fire',
                                                'The Order of the Phoenix',
                                                'The Half-Blood Prince',
                                                'The Deathly Hallows']})

library.books_available.update({'John Smith': ['Money', 'Invest', 'Stocks']})


library.get_book("John Smith", "Money", 20, user1)
print(user1.books_rent)
library.get_book("John Smith", "Money", 20, user2)
library.get_book('John Smith', 'Invest', 20, user2)

# registration.change_username(12, "Georgi Kirilov", library)


for key, value in library.rented_books.items():
    print(key)
    print(value)