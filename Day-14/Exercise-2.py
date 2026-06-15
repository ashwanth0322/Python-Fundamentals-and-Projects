#Adding features to child class
class Person():


    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print("Name : ",self.name)
        print("Age : ",self.age)

    
class student(Person):
    
    def study(self):
        print(self.name,"is studying")

s1=student("Ash",19)
s1.display()
s1.study()