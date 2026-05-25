class Loan:

    def __init__(self, loan_id, book, member):

        self.__loan_id = loan_id
        self.__book = book
        self.__member = member
        self.__is_active = True

    @property
    def loan_id(self):
        return self.__loan_id

    @property
    def book(self):
        return self.__book

    @property
    def member(self):
        return self.__member

    @property
    def is_active(self):
        return self.__is_active

    def close_loan(self):
        self.__is_active = False