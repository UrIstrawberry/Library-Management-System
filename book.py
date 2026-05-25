class Book:

    def __init__(self, book_id, title, author):

        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__available = True

    @property
    def book_id(self):
        return self.__book_id

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def available(self):
        return self.__available

    def borrow(self):
        self.__available = False

    def return_book(self):
        self.__available = True