from library_service import LibraryService


def display_menu():

    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")

    print("1. Add Book")
    print("2. Register Member")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. View Books")
    print("6. View Members")
    print("7. View Loans")
    print("8. Exit")


def main():

    service = LibraryService()

    while True:

        display_menu()

        choice = input("Enter choice: ")

        if choice == "1":
            service.add_book()

        elif choice == "2":
            service.register_member()

        elif choice == "3":
            service.borrow_book()

        elif choice == "4":
            service.return_book()

        elif choice == "5":
            service.view_books()

        elif choice == "6":
            service.view_members()

        elif choice == "7":
            service.view_loans()

        elif choice == "8":

            print("Program closed.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
