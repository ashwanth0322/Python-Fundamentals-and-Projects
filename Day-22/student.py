#Creating code to combine oop and file handlig
class Student:
    
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no

    def save_to_file(self):
        with open("student.txt","a") as file:
            file.write(f"{self.name},{self.roll_no}\n")


    def read_file(self):
        with open("student.txt","r") as file:
            for line in file:
                data=line.split(",")
                print("Name :",data[0])
                print("Roll no :",data[1])