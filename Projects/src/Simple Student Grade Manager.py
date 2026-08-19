# Add student names and marks
# Calculate grades
# Display all students
# Find the class average
# Use Python data types, conditions, loops, and statements

# Simple Student Grade Manager

# A list stores multiple student records
students = []

# A tuple stores fixed grade information
grade_letters = ("A", "B", "C", "D", "F")


def calculate_grade(mark):
    """Calculate a grade using conditions."""
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "F"


def add_student():
    """Add a student to the list."""
    name = input("Enter student name: ").strip()

    # Check that the name is not empty
    if name == "":
        print("Name cannot be empty.")
        return

    try:
        mark = float(input("Enter student mark from 0 to 100: "))

        # Check whether the mark is valid
        if mark < 0 or mark > 100:
            print("Mark must be between 0 and 100.")
            return

        grade = calculate_grade(mark)

        # A dictionary stores information about one student
        student = {
            "name": name,
            "mark": mark,
            "grade": grade,
            "passed": mark >= 60
        }

        students.append(student)
        print(f"{name} was added successfully.")

    except ValueError:
        print("Please enter a valid number.")


def display_students():
    """Display all students."""
    if len(students) == 0:
        print("No students have been added yet.")
        return

    print("\nStudent List")
    print("-" * 40)

    # A for loop displays every student
    for number, student in enumerate(students, start=1):
        result = "Passed" if student["passed"] else "Failed"

        print(
            f"{number}. {student['name']} | "
            f"Mark: {student['mark']:.2f} | "
            f"Grade: {student['grade']} | "
            f"{result}"
        )


def show_statistics():
    """Display class statistics."""
    if not students:
        print("No student data available.")
        return

    total_marks = 0.0
    passed_students = 0

    # Loop through the students and calculate statistics
    for student in students:
        total_marks += student["mark"]

        if student["passed"]:
            passed_students += 1

    average = total_marks / len(students)

    print("\nClass Statistics")
    print("-" * 40)
    print(f"Number of students: {len(students)}")
    print(f"Class average: {average:.2f}")
    print(f"Passed students: {passed_students}")
    print(f"Failed students: {len(students) - passed_students}")


def search_student():
    """Search for a student by name."""
    if not students:
        print("No students available.")
        return

    search_name = input("Enter the student name to search: ").strip().lower()
    found = False

    for student in students:
        if student["name"].lower() == search_name:
            print("\nStudent Found")
            print(f"Name: {student['name']}")
            print(f"Mark: {student['mark']}")
            print(f"Grade: {student['grade']}")
            print(f"Passed: {student['passed']}")

            found = True
            break

    if not found:
        print("Student was not found.")


def show_grade_letters():
    """Display the tuple of grade letters."""
    print("\nAvailable grade letters:")
    
    # Another for loop
    for letter in grade_letters:
        print(letter, end=" ")

    print()


# Main program
def main():
    # A Boolean variable controls the while loop
    running = True

    while running:
        print("\n===== Student Grade Manager =====")
        print("1. Add student")
        print("2. Display students")
        print("3. Show statistics")
        print("4. Search for a student")
        print("5. Show grade letters")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            display_students()

        elif choice == "3":
            show_statistics()

        elif choice == "4":
            search_student()

        elif choice == "5":
            show_grade_letters()

        elif choice == "6":
            print("Thank you for using the program.")
            running = False

        else:
            print("Invalid choice. Please select a number from 1 to 6.")


# Start the program
if __name__ == "__main__":
    main()
