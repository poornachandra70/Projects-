marks = int(input("Enter marks: "))
attendance = int(input("Enter attendance: "))

if marks >= 35 and (attendance >= 75 or marks >= 80):
    print("Pass")
else:
    print("Fail")