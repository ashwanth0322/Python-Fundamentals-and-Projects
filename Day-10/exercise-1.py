try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))

    div=num1/num2
    print(div)

except ValueError:
    print("Please enter a valid integer")

except ZeroDivisionError:
    print("It cant be divided by Zero")


print("program finished")
