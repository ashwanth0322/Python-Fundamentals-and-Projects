#Creating code to combine oop and file handlig
class Student:
    
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no

    def save_to_file(self):
        with open("student.txt","w") as file:
            file.write(f"Name of the student is {self.name}, Roll no is {self.roll_no}\n")
    
    def read_file(self):
        with open("student.txt","r") as file:
            data=file.read()
            print(data)


