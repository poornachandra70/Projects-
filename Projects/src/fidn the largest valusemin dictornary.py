marks = {
    "Rahul": 75,
    "Amit": 89,
    "Ravi": 67,
    "Kiran": 92
}

highest = max(marks, key=marks.get)

print("Highest marks:", highest)
print("Marks:", marks[highest])