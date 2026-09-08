password = input("Enter password: ")

if len(password) >= 8:
    if len(password) <= 20:
        print("Valid password length")
    else:
        print("Password too long")
else:
    print("Password too short")