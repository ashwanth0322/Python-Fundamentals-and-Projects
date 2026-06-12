#creating version 2 of expense total calculator 
no=int(input("Enter the no of expenses:"))
expenses=[]
total=0
for i in range(no):
    cost=int(input("Enter the cost of item:"))
    expenses.append(cost)

for expense in expenses:
    total+=expense
print("Total expense :",total)