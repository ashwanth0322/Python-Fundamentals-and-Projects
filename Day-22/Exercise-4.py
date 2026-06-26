#Creating a program to learn the file handling
with open("students.txt","w") as file:
    for i in range(3):
        name=input("Enter the name :")
        file.write(f"{name}\n")

with open("students.txt","r") as file:
    data=file.read()
    print(data)
