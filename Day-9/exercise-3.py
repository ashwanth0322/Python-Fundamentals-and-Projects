#creating an advanced version of expense calculator 
expenses=[]
while True:
    print("\n1. Add Expense")
    print("2. View Expense")
    print("3. Total Expense")
    print("4. Exit")

    choice=input("Enter the menu you want to operate:")

    if choice == "1":
        print("You have selected Add Expenses Menu")
        while True:
            expense=input("Enter the expense and type done after completing :")
            if expense == "done":
                break
            expenses.append(int(expense))

    elif choice == "2":
        print("You Have Selected View Menu")
        print("Expenses :",expenses)

    elif choice == "3":
        print("You Have Selected total expenses Menu")
        print("Total Expenses :",sum(expenses))

    elif choice == "4":
        print("Thank You For Using Our Website")
        break
    else:
        print("Please Choose a Proper Menu")

        
    

