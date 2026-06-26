#Creating a program that asks name from the user and saves in a file 
with open("users.txt","w") as file:
    name=input("Enter the name :")
    file.write(name)

with open("users.txt","r") as file:
    file=file.read()
    print("Saved name :",file)
