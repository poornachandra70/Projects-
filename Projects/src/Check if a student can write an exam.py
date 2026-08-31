attendance = int(input("Enter attendance percentage: "))
fees = input("Are fees paid? (yes/no): ")

if attendance >= 75 and fees == "yes":
    print("Student can write the exam.")
else:
    print("Student cannot write the exam.")