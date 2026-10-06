class Employee:

    def show_company(self):
        print("Company: ABC Technologies")


class Developer(Employee):

    def work(self):
        print("Developer writes code")


class Tester(Employee):

    def work(self):
        print("Tester tests software")


developer = Developer()
tester = Tester()

developer.show_company()
developer.work()

tester.show_company()
tester.work()