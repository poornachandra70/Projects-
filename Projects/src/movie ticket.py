age = int(input("Enter age: "))
member = input("Member? ")

if age >= 18 and (member == "yes" or age >= 60):
    print("Special ticket")
else:
    print("Normal ticket")