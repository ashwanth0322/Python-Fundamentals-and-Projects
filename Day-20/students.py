#Importing the student module to create student record system
from student import Student

students=[]
while True:
    print("1. Add Student")
    print("2. View student")
    print("3. Search student")
    print("4. Exit")
    menu=int(input("Enter the menu:"))

    if menu == 1:
        name=input("Enter the name of the student :")
        roll_no=int(input("Enter the roll number of the student :"))
        s=Student(name,roll_no)
        students.append(s)
        print("Object Added")
    elif menu == 2:
        for i in students:
            i.display_info()
    elif menu == 3:
        search=int(input("Enter the roll no of student:"))
        found=False
        for i in students:
            if i.roll_no == search:
                i.display_info()
                found=True
        if found == False:
                print("No Student Found")

    elif menu == 4:
        print("Thank you for visiting")
        break
        
    


