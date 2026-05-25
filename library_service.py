from book import Book
from member import Member
from loan import Loan

from exceptions import (
    BookNotFoundError,
    MemberNotFoundError,
    BookUnavailableError,
    LoanNotFoundError,
    LoanAlreadyClosedError
)


class LibraryService:

    def __init__(self):

        self.__books = {}
        self.__members = {}
        self.__loans = []

    def add_book(self):

        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        author = input("Enter Book Author: ")

        book = Book(book_id, title, author)

        self.__books[book.book_id] = book

        print(f"Book added: {title}")

    def register_member(self):

        member_id = input("Enter Member ID: ")
        name = input("Enter Member Name: ")
        email = input("Enter Member Email: ")

        member = Member(member_id, name, email)

        self.__members[member.member_id] = member

        print(f"Member registered: {name}")

    def borrow_book(self):

        try:

            book_id = input("Enter Book ID: ")
            member_id = input("Enter Member ID: ")

            book = self.__books.get(book_id)

            if book is None:
                raise BookNotFoundError("Book not found.")

            member = self.__members.get(member_id)

            if member is None:
                raise MemberNotFoundError("Member not found.")

            if not book.available:
                raise BookUnavailableError(
                    "Book is already borrowed."
                )

            loan_id = f"L{len(self.__loans) + 1:03}"

            book.borrow()

            loan = Loan(loan_id, book, member)

            self.__loans.append(loan)

            print(f"{member.name} borrowed {book.title}")

        except (
            BookNotFoundError,
            MemberNotFoundError,
            BookUnavailableError
        ) as error:

            print(error)

    def return_book(self):

        try:

            loan_id = input("Enter Loan ID: ")

            loan_found = None

            for loan in self.__loans:

                if loan.loan_id == loan_id:
                    loan_found = loan
                    break

            if loan_found is None:
                raise LoanNotFoundError("Loan not found.")

            if not loan_found.is_active:
                raise LoanAlreadyClosedError(
                    "Book already returned."
                )

            loan_found.book.return_book()

            loan_found.close_loan()

            print(
                f"{loan_found.member.name} returned "
                f"{loan_found.book.title}"
            )

        except (
            LoanNotFoundError,
            LoanAlreadyClosedError
        ) as error:

            print(error)

    def view_books(self):

        books = list(self.__books.values())

        if len(books) == 0:
            print("No books found.")
            return

        print("\nBooks:\n")

        for book in books:

            status = "Available"

            if not book.available:
                status = "Borrowed"

            print(
                f"{book.book_id} - "
                f"{book.title} by "
                f"{book.author} [{status}]"
            )

    def view_members(self):

        members = list(self.__members.values())

        if len(members) == 0:
            print("No members found.")
            return

        print("\nMembers:\n")

        for member in members:

            print(
                f"{member.member_id} - "
                f"{member.name} ({member.email})"
            )

    def view_loans(self):

        loans = list(self.__loans)

        if len(loans) == 0:
            print("No loans found.")
            return

        print("\nLoans:\n")

        for loan in loans:

            status = "Closed"

            if loan.is_active:
                status = "Active"

            print(
                f"{loan.loan_id} - "
                f"{loan.member.name} borrowed "
                f"{loan.book.title} [{status}]"
            )