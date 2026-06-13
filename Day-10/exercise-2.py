#Creating an calculator 
print("1. Add Operation")
print("2. subtract Operation")
print("3. Multiplication Operation")
print("4. Division Operation ")
choice=input("Enter the choice :")
try:
    num1=int(input("Enter a no :"))
    num2=int(input("Enter a no :"))
    
    if choice == "1":
        sum=num1+num2
        print("sum = ",sum)
    
    elif choice == "2":
        sub=num1-num2
        print("Sub = ",sub)

    elif choice == "3" :
        pro=num1*num2
        print("Product = ",pro)

    elif choice == "4" :
        quo=num1/num2
        print("Quotient = ",quo)

    else:
        print("Please Choose A Valid Choice")

except ValueError:
    print("Please Enter a Valid Integer")

except ZeroDivisionError:
    print("It cant be divided by zero")

finally:
    print("Caluculator closed")

