#Creating a code to understand Ecapsulation
class Student():

    def __init__(self,name,marks):
        self.name=name
        self._marks=marks

    def display_info(self):
        print("Name :",self.name)
        print("Marks :",self._marks)

s1=Student("Ash",90)
s1.display_info()    