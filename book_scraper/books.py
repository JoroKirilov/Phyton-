class Book:
    def __init__(self, tittle, price):
        self.__tittle = tittle
        self.__price = price

    def __str__(self):
        return f"Tittle: {self.__tittle}\nPrice: {self.__price}"


class BookCounter:
    def __init__(self, number_of_desired_books):
        self.__list_of_books = []
        self.__curr_number_of_books = 0
        self.__desired_number_of_books = number_of_desired_books

    def add_a_book(self, book):
        self.__list_of_books.append(book)
        self.__curr_number_of_books += 1

    def if_number_reached(self):
        return self.__curr_number_of_books == self.__desired_number_of_books

    def print_info(self):
        for book in self.__list_of_books:
            print(book)
