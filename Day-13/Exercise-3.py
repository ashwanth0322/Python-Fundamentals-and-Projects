#Creating a prototype bank website using encapsulation
class Bankaccount():

    def __init__(self,owner,balance):
        self.owner=owner
        self.__balance=balance

    
    def get_balance(self):
        print("Current Balance :",self.__balance)
    
    def deposit(self,amount):
        if amount >= 0:
            self.__balance+=amount
            print("Balance After Deposit :",self.__balance)
        else:
            print("Invalid amount")

    def withdraw(self,amount):
        if amount <= self.__balance:
            self.__balance-=amount
            print("Balance After Withdraw :",self.__balance)
        else:
            print("Insufficient Balance")

s1=Bankaccount("Ash",1000)
s1.get_balance()
s1.deposit(500)
s1.withdraw(1000)
s1.withdraw(2000)
s1.deposit(-50)