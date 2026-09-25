contacts = {}

while True:
    print("\n----- Contact Manager -----")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Show Contacts")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")

        contacts[name] = phone

        print("Contact saved.")

    elif choice == "2":
        name = input("Enter name: ")

        if name in contacts:
            print("Phone:", contacts[name])
        else:
            print("Contact not found.")

    elif choice == "3":
        for name, phone in contacts.items():
            print(name, ":", phone)

    elif choice == "4":
        print("Program closed.")
        break

    else:
        print("Invalid choice.")