#Creating a program with getter and setter
class Student():

    def __init__(self,name,cgpa):
        self.name=name
        self.__cgpa=cgpa

    
    def display(self):
        print("Name : ",self.name)
        print("Cgpa : ",self.__cgpa)

    
    def get_cgpa(self):
        return self.__cgpa
    
    def set_cgpa(self,cgpa):
        if 0<= cgpa <= 10 :
            self.__cgpa=cgpa
        else:
             print("Acess Denied")

s1=Student("Ash",9.0)
s1.display()
print(s1.get_cgpa())
s1.set_cgpa(8.3)
s1.display()
print(s1.get_cgpa())
s1.set_cgpa(89)