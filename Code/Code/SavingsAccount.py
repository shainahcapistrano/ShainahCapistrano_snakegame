from BankAccount import *

class SavingsAccount (BankAccount):

    def __init__(self, owner,aNumber, interest_rate):
        super().__init__(owner, aNumber)
        self.interest_rate = interest_rate

    def payInterest(self):
        # self.balance += self.balance * self.interest_rate
        super().deposit(super().getBalance() * self.interest_rate)


    def withdraw(self, amount):
        super().withdraw(amount + .50)


    def __str__(self):
        out = super().__str__()
        out += " with interest rate " + str(self.interest_rate)
        return out

 
def test():
    print("tester")
    savings1 = SavingsAccount("Suzy", 789, .1)
    bank1 = BankAccount("Sam", 456)
    savings1.deposit(100)
    bank1.deposit(100)
    print(savings1)
    print(bank1)
    # savings1.payInterest()
    savings1.withdraw(10)
    bank1.withdraw(10)
    # bank1.payInterest()
    print(savings1)
    print(bank1)



if __name__ == "__main__":
    test()
