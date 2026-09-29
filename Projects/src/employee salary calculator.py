class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_bonus(self):
        bonus = self.salary * 0.10
        return bonus

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Bonus:", self.calculate_bonus())


employee = Employee("Amit", 30000)
employee.display()