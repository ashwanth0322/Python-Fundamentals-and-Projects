#Create a program using private attribute
class BankAccount():

    def __init__(self,balance):
        self.__balance=balance

    def display_info(self):
        print("Balance :",self.__balance)

account1=BankAccount(10000)
account1.display_info()
print(account1.__balance)