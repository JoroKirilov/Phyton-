from Inheritance.homework_steering_wheel.library.user import User


class Library:
    def __init__(self):
        self.user_record = []
        self.books_available = {}
        self.rented_books = {}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User):
        if author in self.books_available:
            if book_name in self.books_available[author]:
                user.take_book(book_name)
                if user.username in self.rented_books:
                    self.rented_books[user.username].update({book_name: days_to_return})
                else:
                    self.rented_books = {user.username: {book_name: days_to_return}}
                del self.books_available[book_name]
                return f"{book_name} successfully rented for the next {days_to_return} days!"
        return f"The book {book_name} is already rented and will be available in {days_to_return} days rented by {user.username}!"

    def return_book(self, author: str, book_name: str, user: User):
        if book_name in user.books_rent:
            if author not in self.books_available:
                self.books_available = {author: []}
                self.books_available[author].append(book_name)
            else:
                self.books_available[author].append(book_name)

            for key, value in self.rented_books.items():
                if book_name in value.keys():
                    del self.rented_books[key][book_name]

            user.books_rent.remove(book_name)
        else:
            print(f"{user.username} doesn't have this book in his/her records!")



