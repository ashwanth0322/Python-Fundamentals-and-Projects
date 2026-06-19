#Creating Employee system using polymorphism 
class Employee():

    def __init__(self,name):
        self.name=name

    
    def work(self):
        print("Employees are working")


class Manager(Employee):

    def work(self):
        print(self.name,"is managing the team")

class Developer(Employee):

    def work(self):
        print(self.name,"is writing code")

class Tester(Employee):

    def work(self):
        print(self.name,"is testing the software")

Employees=[Manager("Ash"),Developer("Pradeep"),Tester("Rahul")]
for employee in Employees:
    employee.work()