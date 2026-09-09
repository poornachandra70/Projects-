while True:
    print("1. Hello")
    print("2. Bye")
    print("3. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        print("Hello Bro!")
    elif choice == 2:
        print("Bye Bro!")
    elif choice == 3:
        break
    else:
        print("Invalid choice")