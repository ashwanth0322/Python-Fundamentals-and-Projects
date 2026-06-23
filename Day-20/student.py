#Creating class student to display student name and roll no 
class Student():

    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no

    def display_info(self):
        print("Name :",self.name)
        print("Roll Number :",self.roll_no)

        