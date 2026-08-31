age = int(input("Enter your age: "))
has_id = input("Do you have an ID proof? (yes/no): ")

if age >= 18 and has_id == "yes":
    print("Eligible for a driving license.")
else:
    print("Not eligible for a driving license.")