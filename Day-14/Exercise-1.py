#Inheritance
class Person():


    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print("Name : ",self.name)
        print("Age : ",self.age)

    
class student(Person):
    pass

s1=student("Ash",19)
s1.display()