#Creating a bank website using private attribute 
class BankAccount():

    def __init__(self,balance):
        self.__balance=balance
        

    def deposit(self,amount):
        if amount > 0:
            self.__balance+=amount
        else:
            print("Enter Valid Amount")

    def withdraw(self,amount):
        if self.__balance >= amount and amount > 0:
            self.__balance-=amount
        else:
            print("Enter A Valid Amount")

    def show_balance(self):
        return self.__balance

account_1=BankAccount(10000)
b1=account_1.show_balance()
print("Current Balance :",b1)
account_1.deposit(5000)
b2=account_1.show_balance()
print("Balance After Deposit :",b2)
account_1.withdraw(10000)
b3=account_1.show_balance()
print("Balance after Withdraw :",b3)
account_1.deposit(-100)
account_1.withdraw(-500)
