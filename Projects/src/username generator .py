first_name = input("Enter first name: ").lower()
last_name = input("Enter last name: ").lower()
year = input("Enter birth year: ")

username1 = first_name + year
username2 = first_name + "_" + last_name
username3 = first_name[:3] + last_name[:3] + year

print("\n===== GENERATED USERNAMES =====")
print("Username 1:", username1)
print("Username 2:", username2)
print("Username 3:", username3)