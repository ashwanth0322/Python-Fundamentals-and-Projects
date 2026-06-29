#Creating a program to import the module that is alraeady created 
import student
name=input("Enter a name :")
roll_no=int(input("Enter the roll no :"))
s1=student.Student(name,roll_no)
s1.save_to_file()
s1.read_file()
print("Student Saved Successfully")