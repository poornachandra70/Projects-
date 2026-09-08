age = int(input("Enter age: "))

if age >= 18:
    if age >= 60:
        print("Senior citizen")
    else:
        print("Adult")
else:
    print("Minor")