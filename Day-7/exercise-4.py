#reading a file without calling it 
with open("notes.txt","r") as file:
    content=file.read()
    print(content)