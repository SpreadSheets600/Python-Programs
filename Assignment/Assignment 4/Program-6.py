books = {101: "Python Programming", 102: "Data Structures", 103: "Algorithms"}


def add_book(book_id, book_name):
    if book_id in books:
        print(f"Book ID {book_id} Already Exists!")

    else:
        books[book_id] = book_name
        print(f"Book '{book_name}' Added With ID {book_id}")


def remove_book(book_id):
    if book_id in books:
        removed = books.pop(book_id)
        print(f"Book '{removed}' With ID {book_id} Removed")

    else:
        print("Book ID Not Found!")


def search_book(book_id):
    if book_id in books:
        print(f"Book Found → ID : {book_id}, Name : {books[book_id]}")

    else:
        print("Book Not Found!")


def display_books():
    if not books:
        print("No Books Available")

    else:
        print("\nList of Books : ")
        for id, name in books.items():
            print(f"ID : {id}, Name : {name}")


def main():
    while True:
        print("\nBook Management System\n")
        print("1. Display Books")
        print("2. Add Book")
        print("3. Remove Book")
        print("4. Search Book")
        print("5. Exit")
        choice = input("Enter Your Choice (1-5) : ")

        if choice == "1":
            display_books()

        elif choice == "2":
            book_id = int(input("Enter Book ID : "))
            book_name = input("Enter Book Name : ")
            add_book(book_id, book_name)

        elif choice == "3":
            book_id = int(input("Enter Book ID To Remove : "))
            remove_book(book_id)

        elif choice == "4":
            book_id = int(input("Enter Book ID To Search : "))
            search_book(book_id)

        elif choice == "5":
            print("Exiting ...")
            break
        else:
            print("Invalid Choice. Please Try Again.")


if __name__ == "__main__":
    main()  # To Make It Run Only When File Is Ran
