age = int(input("Enter your age: "))
ticket = input("Do you have a ticket? (yes/no): ")

if age >= 18 and ticket == "yes":
    print("You can enter the movie.")
else:
    print("You cannot enter the movie.")