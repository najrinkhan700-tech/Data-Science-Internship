class  BankAccount:
    def __init__(self,name,balance,pin):
        self.name = name
        self._balance = balance
        self.__pin = pin

    def showDetails(self):
        print("name:",self.name)
        print("Balance:",self._balance)
    
    def __showPin(self):
        print("PIn:",self.__pin)

    def access_pin(self):
        self.__showPin()

#child class
class ATM(BankAccount):
    def withdraw(self,amount):
        if amount <= self._balance:
            self._balance -= amount
            print("Amount withdraw successful")
            print("Reamaining balance:",self._balance)
        
        else:
            print("Insufficeint balance")
        
#objaect creation 
# first object of bank account
a = ATM("Rahul",5000,1234)
a.showDetails()
a.withdraw(1000)
a.access_pin()