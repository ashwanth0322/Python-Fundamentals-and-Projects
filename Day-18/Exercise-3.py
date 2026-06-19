#Creating a Payment processing system using polymorphism
class Payment():

    def process_payment():
        print("processing payment")

class Upi(Payment):

    def process_payment(self):
        print("Upi is processing payment")

class Credit_Card(Payment):

    def process_payment(self):
        print("Credit Card is processing payment")

class Net_Banking(Payment):

    def process_payment(self):
        print("Net Banking is processing payment")

payments=[Upi(),Credit_Card(),Net_Banking()]
for payment in payments:
    payment.process_payment()