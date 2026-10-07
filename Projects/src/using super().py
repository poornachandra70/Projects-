class Parent:

    def display(self):
        print("This is parent class")


class Child(Parent):

    def display(self):

        # Calling parent method
        super().display()

        print("This is child class")


child = Child()

child.display()