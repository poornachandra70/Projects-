names = ["Rahul", "Ravi", "Kiran", "Arjun", "Raju"]

search = "Kiran"

for name in names:
    if name == search:
        print("Name found")
        break
    else:
        print("Checking:", name)