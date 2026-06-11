#using loop in the file handling 
with open("subjects.txt","w") as file:
    file.write("Python\nSql\nFastAPI\n")
    
with open("subjects.txt","r") as file:
        for line in file:
            print(line.strip())