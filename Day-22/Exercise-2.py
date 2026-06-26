#creating a new file and writing the content through with open method
with open("notes.txt","w") as file:
    file.write("Python\n")
    file.write("OOP")
    file.write("File Handling")
