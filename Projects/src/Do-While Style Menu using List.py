fruits = ["Apple", "Banana", "Mango"]

while True:
    print("\n1. Show Fruits")
    print("2. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print(fruits)

    elif choice == "2":
        print("Program ended")
        break

    else:
        print("Invalid choice")