books = []


def add_book():
    name = input("Enter book name: ")
    author = input("Enter author name: ")

    books.append({
        "name": name,
        "author": author,
        "available": True
    })

    print("Book added successfully!")


def view_books():
    if len(books) == 0:
        print("No books available.")
        return

    print("\n--- Library Books ---")

    for i, book in enumerate(books, start=1):
        status = "Available" if book["available"] else "Borrowed"

        print(f"{i}. {book['name']} - {book['author']} - {status}")


def search_book():
    search = input("Enter book name to search: ").lower()

    found = False

    for book in books:
        if search in book["name"].lower():
            status = "Available" if book["available"] else "Borrowed"

            print(f"Book: {book['name']}")
            print(f"Author: {book['author']}")
            print(f"Status: {status}")

            found = True

    if not found:
        print("Book not found.")


def borrow_book():
    name = input("Enter book name to borrow: ").lower()

    for book in books:
        if book["name"].lower() == name:

            if book["available"]:
                book["available"] = False
                print("Book borrowed successfully!")
            else:
                print("Sorry, this book is already borrowed.")

            return

    print("Book not found.")


def return_book():
    name = input("Enter book name to return: ").lower()

    for book in books:
        if book["name"].lower() == name:

            if not book["available"]:
                book["available"] = True
                print("Book returned successfully!")
            else:
                print("This book was not borrowed.")

            return

    print("Book not found.")


while True:

    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Borrow Book")
    print("5. Return Book")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        view_books()

    elif choice == "3":
        search_book()

    elif choice == "4":
        borrow_book()

    elif choice == "5":
        return_book()

    elif choice == "6":
        print("Thank you for using the Library Management System!")
        break

    else:
        print("Invalid choice. Please try again.")