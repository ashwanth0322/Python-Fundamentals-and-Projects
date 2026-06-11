#creating a student record viewer using file handling 
with open("students.txt","r") as file:
    count=0
    for line in file:
        data=line.strip().split(",")
        print("Name:",data[0])
        print("Age:",data[1])
        print("Cgpa:",data[2])
        print()
        count+=1
    print("Total Students :",count)