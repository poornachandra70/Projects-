books = [
    "Python",
    "Java",
    "SQL",
    "HTML",
    "JavaScript"
]

while True:
    print("\n----- Library -----")
    print("1. Show Books")
    print("2. Search Book")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        for book in books:
            print("-", book)

    elif choice == "2":
        search = input("Enter book name: ")

        if search in books:
            print("Book is available.")
        else:
            print("Book not found.")

    elif choice == "3":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")