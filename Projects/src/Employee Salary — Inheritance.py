class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_employee(self):
        print("Name:", self.name)
        print("Salary:", self.salary)


class Developer(Employee):

    def programming(self):
        print(self.name, "is writing Python code")


developer = Developer("Rahul", 40000)

developer.display_employee()
developer.programming()