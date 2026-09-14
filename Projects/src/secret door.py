name = input("Enter your name: ")
password = input("Enter password: ")

if name == "admin":
    if password == "1234":
        print("Secret door opened!")
    else:
        print("Wrong password")
else:
    print("Unknown user")