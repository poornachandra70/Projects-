age = int(input("Enter your age: "))

if age >= 18:
    test = input("Did you pass the driving test? (yes/no): ")

    if test == "yes":
        print("You can get a driving license")
    else:
        print("You need to pass the driving test")
else:
    print("You are too young")