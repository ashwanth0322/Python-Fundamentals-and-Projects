#Creating a student management system
class Person():

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display_info(self):
        print("Name :",self.name)
        print("Age :",self.age)

class Student(Person):

    def __init__(self, name, age,roll_no):
        super().__init__(name, age)
        self.roll_no=roll_no

    def display_info(self):
         super().display_info()
         print("Roll No :",self.roll_no)

s1=Student("Ash",19,193)
s1.display_info()