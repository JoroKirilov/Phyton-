class User:
    def __init__(self, user_id: int, username: str):
        self.user_id = user_id
        self.username = username
        self.books_rent = []

    def info(self, book: str):
        # result = (', '.join(books))
        # return result
        return book

    def __str__(self):
        return f"User : {self.user_id}, {self.username}, Books rented : {self.books_rent}"

    def take_book(self, book: str):
        self.books_rent.append(book)
        self.info(book)
