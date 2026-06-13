import Module
print("1. Add")
print("2. subtract")
print("3. Multiply")
print("4. Division")
try:
    num1=int(input("Enter a no: "))
    num2=int(input("Enter a no: "))
    choice=int(input("Enter a choice: "))
    if choice == 1:
        sum=Module.add(num1,num2)
        print("The Sum = ",sum)
    elif choice == 2:
        dif=Module.sub(num1,num2)
        print("The Difference = ",dif)
    elif choice == 3:
        pro=Module.mul(num1,num2)
        print("The Product = ",pro)
    elif choice == 4:
        quo=Module.div(num1,num2)
        print("The Quotient = ",quo)
    else:
        print("Enter a Valid Choice")
except ValueError:
    print("Please Enter a Proper Value")
except ZeroDivisionError:
    print("It cant be divided by zero")
finally:
    print("The Calculator is Closed")