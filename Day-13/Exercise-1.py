#Creating a program using encapsulation
class Student():

    def __init__(self,name,cgpa):
        self.name=name
        self.__cgpa=cgpa


    def dispaly(self):
        print("Name : ",self.name)
        print("Cgpa : ",self.__cgpa)

    

s1=Student("Ash",9.0)
s1.dispaly()
