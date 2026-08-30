amount = float(input("Enter purchase amount: "))
member = input("Are you a member? (yes/no): ")

if amount >= 5000 or member == "yes":
    print("You are eligible for a discount")
else:
    print("No discount")