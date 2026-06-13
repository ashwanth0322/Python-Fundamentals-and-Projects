#creating a notes app using file handling 
mode=int(input("choose the mode(1or2): "))
if mode == 1:
    print("1. add the content")
    content=input("enter the content to be entered: ")
    with open("notes.txt","a") as file:
        file.write(f"{content}\n")
elif mode == 2:
    print("2. view the content")
    with open("notes.txt","r") as file:
        content=file.read()
        print(content)
else:
    print("not an valid option")