class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_employee(self):
        print("Name:", self.name)
        print("Salary:", self.salary)


class Manager(Employee):
    def display_manager(self):
        print("Position: Manager")


manager = Manager("Rahul", 50000)

manager.display_employee()
manager.display_manager()