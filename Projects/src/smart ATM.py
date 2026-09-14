balance = 5000
amount = int(input("Enter withdrawal amount: "))

if amount > 0:
    if amount <= balance:
        print("Withdrawal successful")
        print("Remaining balance:", balance - amount)
    else:
        print("Insufficient balance")
else:
    print("Invalid amount")