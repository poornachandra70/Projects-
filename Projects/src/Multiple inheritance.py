class Employee:
    def employee_details(self):
        print("Employee Name: Rahul")


class Developer:
    def developer_details(self):
        print("Role: Python Developer")


class TeamLead(Employee, Developer):
    def teamlead_details(self):
        print("Position: Team Lead")


person = TeamLead()

person.employee_details()
person.developer_details()
person.teamlead_details()