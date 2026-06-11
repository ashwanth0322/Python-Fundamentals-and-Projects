#using loop and split() in file handling 
with open("students.txt","w") as file:
    file.write("Ash,19,8.5\nPra,20,9.1\nRam,18,8.2\n")
with open("students.txt","r") as file:
    for line in file:
        data=line.strip().split(",")
        if int(data[1]) >= 19 :
            print("Name :",data[0])
            print("Age :",data[1])
            print("Cgpa :",data[2])