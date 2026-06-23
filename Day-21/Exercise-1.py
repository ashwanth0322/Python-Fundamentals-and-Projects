#Creating a student mark analyser
marks=[]
while True:
    try:
        print("")
        print("")
        print("")
        print("1. Add Marks")
        print("2. View Marks")
        print("3. Calcuate Average")
        print("4. Find Highest Mark")
        print("5. Exit")

        menu=int(input("Enter the Menu :"))
        if menu == 1:
            mark=int(input("Enter the mark :"))
            marks.append(mark)
        elif menu == 2:
            if len(marks) >= 0:
                for i in marks:
                    print("Marks :",i)
            else:
                print("Please Add Elements")
        elif menu == 3:
            total=0
            if len(marks) > 0:
                for i in marks:
                    total+=i
                avg=total/len(marks)
                print("Average Mark :",avg)
            else:
                print("Please Add elemnts in List")
        elif menu == 4:
            if len(marks) > 0:
                lar=max(marks)
                print("Largest Element :",lar)
        elif menu == 5:
            print("Thank You for Visiting")
            break
        else:
            print("Choose a Valid Menu")
    except ValueError:
        print("Please Enter a Valid Integer")
    