'''
Write a program which contains one class named as BankAccount. 
BankAccount class contains two instance variables as Name & Amount. 
That class contains one class variable as ROI which is initialise to 10.5. 
Inside init method initialise all name and amount variables by accepting the values from user. 
There are Four instance methods inside class as Display(), Deposit(), Withdraw(), 
CalculateIntrest(). 
Deposit() method will accept the amount from user and add that value in class instance variable 
Amount. 
Withdraw() method will accept amount to be withdrawn from user and subtract that amount 
from class instance variable Amount. 
CalculateIntrest() method calculate the interest based on Amount by considering rate of interest 
which is Class variable as ROI. 
And Display() method will display value of all the instance variables as Name and Amount. 
After designing the above class call all instance methods by creating multiple objects. 
'''


class BankAccount:
    ROI = 10.5

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def deposit(self, depositAmount):
        self.amount += depositAmount

    def withdraw(self, withdrawalAmount):
        self.amount -= withdrawalAmount

    def calculateInterest(self, period):
        return (self.amount * period * BankAccount.ROI) / 100

    def display(self):
        print("Name : ", self.name)
        print("Amount : ", self.amount)


def main():
    obj1 = BankAccount("AAAAA", 2000)
    obj1.withdraw(200)
    obj1.display()
    obj1.deposit(500)
    obj1.display()
    period = int(input("Enter the number of years to calculate interest: "))
    print("Interest calculated for " + obj1.name +
          " is : " + str(obj1.calculateInterest(period)))

    obj2 = BankAccount("BBBBB", 5000)
    obj2.withdraw(300)
    obj2.display()
    obj2.deposit(1000)
    obj2.display()
    period = int(input("Enter the number of years to calculate interest: "))
    print("Interest calculated for " + obj2.name +
          " is : " + str(obj2.calculateInterest(period)))


if(__name__ == "__main__"):
    main()
