username = input()
password = input()
if username == "student":
    if password == "python123":
        print("Login successful")
    else:
        print("Incorrect password")
else:
    print("Incorrect username")