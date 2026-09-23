students = {
    "Rahul": 85,
    "Amit": 45,
    "Kiran": 72,
    "Ravi": 35
}

for name, marks in students.items():
    if marks >= 50:
        print(name, "Passed")