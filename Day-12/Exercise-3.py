#Creating a prototype of bank website using oop
class BankAccount():

    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount

    def show_balance(self):
        print("Current balance :",self.balance)

acc1 = BankAccount("Ash", 1000)

acc1.deposit(500)
acc1.show_balance()

    