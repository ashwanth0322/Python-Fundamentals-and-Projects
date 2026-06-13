#creating a method to check wheather the given data is adult or not 
class Student():

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def is_adult(self):
        if self.age >= 18:
            print(self.name," is an adult")
        else:
            print(self.name," is not an adult")

s1=Student("Ash",19)
s2=Student("Tom",15)
s1.is_adult()
s2.is_adult()
        