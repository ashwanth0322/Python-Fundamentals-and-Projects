#creating an student Management Analyser using oop 
class Student():

    def __init__(self,name,age,cgpa):
        self.name=name
        self.age=age
        self.cgpa=cgpa

    def display_details(self):
        print("Name : ",self.name)
        print("Age : ",self.age)
        print("Cgpa : ",self.cgpa)   

    def  is_eligible(self):
        if self.cgpa >= 8.0:
            print("Eligible for Placement")
        else:
            print("Not Eligible for Placement")

s1=Student("Ash",19,9.0)
s1.display_details()
s1.is_eligible()