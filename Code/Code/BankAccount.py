## Bank Account Class

class BankAccount(object):
    """Models a simple bank account"""
    monthly_fee = 5
    number_of_accounts = 0

    ##Constructor
    def __init__(self, owner, aNumber):
        self.owner = owner
        self.accountNum = aNumber
        self.balance = 0
        BankAccount.number_of_accounts += 1

    @staticmethod
    def update_fee(new_fee):
        BankAccount.monthly_fee = new_fee

    ##Other methods
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            print
            amount += BankAccount.monthly_fee
            self.balance -= 1
        else:
            print("Insufficient funds")
         
    def getBalance(self):
        return self.balance
     
    #Print method
    def __str__(self):
        out = self.owner + " has account number " + str(self.accountNum)
        out = out + " with balance " + str(self.balance)
        return out


     

def testBankAccount():
     print("Test BankAccount class")
     acct = BankAccount("Joe Account", 456)
     acct2 = BankAccount("Suzy Que", 789)
     print(acct)
     acct.deposit(100)
     acct.withdraw(10)
     BankAccount.update_fee(1)
     acct.withdraw(20)
     print("number of account is", BankAccount.number_of_accounts)

if __name__ == "__main__":
    testBankAccount()
    
