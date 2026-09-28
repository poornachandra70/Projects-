balance = 5000
correct_pin = "mona"

pin = input("Enter your PIN: ")

if pin == correct_pin:

    while True:

        print("\n===== ATM =====")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            print("Balance: ₹", balance)

        elif choice == "2":
            amount = float(input("Enter deposit amount: "))

            if amount > 0:
                balance += amount
                print("Amount deposited successfully.")
            else:
                print("Invalid amount.")

        elif choice == "3":
            amount = float(input("Enter withdrawal amount: "))

            if amount <= 0:
                print("Invalid amount.")

            elif amount > balance:
                print("Insufficient balance.")

            else:
                balance -= amount
                print("Please collect your cash.")

        elif choice == "4":
            print("Thank you for using ATM.")
            break

        else:
            print("Invalid choice.")

else:
    print("Incorrect PIN.")