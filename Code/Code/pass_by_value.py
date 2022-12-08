from BankAccount import *

def payBonus(bankAccount, bonus):
    bankAccount.deposit(bonus)


account = BankAccount("JimBob", 234)
payBonus(account, 100)
print(account)
