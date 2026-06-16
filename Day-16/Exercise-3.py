#Creating an Employee management system
class Employee():

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def display_info(self):
        print("Name :",self.name)
        print("salary :",self.salary)

    def work(self):
        print("Employee is Working")

class Manager(Employee):

    def __init__(self,name,salary,team_size):
        super().__init__(name,salary)
        self.team_size=team_size

    def display_info(self):
        super().display_info()
        print("Team Size :",self.team_size)

    def work(self):
        print("Manger is Working")

class Developer(Employee):

    def __init__(self,name,salary,programming_language):
        super().__init__(name,salary)
        self.programming_language=programming_language

    def display_info(self):
        super().display_info()
        print("Programming Language :",self.programming_language)

    def work(self):
        print(f"Developer writing code with {self.programming_language}")

emp_1=Manager("Ash",50000,8)
emp_1.display_info()
emp_1.work()
emp_2=Developer("Pradeep",100000,"Python")
print()
emp_2.display_info()
emp_2.work()