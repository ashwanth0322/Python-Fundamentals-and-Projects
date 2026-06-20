#using a module and creating the calculator 
import Calculations
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Division")


try:
    menu=int(input("Enter the choice:"))
    num_1=int(input("Enter the Number :"))
    num_2=int(input("Enter the Number :"))
    if menu == 1:
        print("Sum :",Calculations.add(num_1,num_2))
    elif menu == 2:
        print("Difference :",Calculations.sub(num_1,num_2))
    elif menu == 3:
        print("product :",Calculations.product(num_1,num_2))
    elif menu == 4:
        print("Quotient :",Calculations.div(num_1,num_2))
    else:
        print("Enter a valid option")
except ValueError:
    print("Enter a Integer Value")
except ZeroDivisionError:
    print("It cant be divided by zero")

