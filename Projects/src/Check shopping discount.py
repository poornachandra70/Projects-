amount = int(input("Enter amount: "))

if amount >= 1000:
    if amount >= 5000:
        print("20% discount")
    else:
        print("10% discount")
else:
    print("No discount")