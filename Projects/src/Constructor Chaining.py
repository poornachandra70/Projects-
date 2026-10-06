class Person:

    def __init__(self, name):
        self.name = name
        print("Person constructor called")


class Student(Person):

    def __init__(self, name, course):
        super().__init__(name)
        self.course = course
        print("Student constructor called")

    def display(self):
        print("Name:", self.name)
        print("Course:", self.course)


student = Student("Rahul", "CSE")

student.display()