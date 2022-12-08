## Polymorphism

from BankAccount import *
#from SavingsAccount import *

def getMoney(account):

    amount = float(input("How much would you like to withdraw? "))
    print(account)
    account.withdraw(amount)
    print(account)


checking = BankAccount(123,"joe")
#savings = SavingsAccount(345, "joe", .05, 100)
checking.deposit(50)
#savings.makeDeposit(50)
getMoney(checking)
#getMoney(savings)
print(checking)
