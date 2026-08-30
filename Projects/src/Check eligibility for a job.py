age = int(input("Enter your age: "))
degree = input("Do you have a degree? (yes/no): ")

if age >= 18 and degree == "yes":
    print("You are eligible for the job")
else:
    print("You are not eligible")