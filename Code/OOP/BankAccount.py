from Person import *

class BankAccount:

    ##Constructor
    def __init__(self, name, account):
         self.owner = name
         self.account_number = account
         self.balance = 0

    ##Class related methods
    def deposit(self, amount):
        self.balance += amount


    def withdraw(self, amount_withdraw):
        if amount_withdraw <= self.balance:
            self.balance -= amount_withdraw
        else:
            print("insufficient funds")



    ##Nice to have method to print things out
    def __str__(self):
        out = str(self.owner) + " has account " + str(self.account_number)
        out = out + " that contains a balance of " + str(self.balance)
        return out


def tester():
    suzy = Person("Suzy Que", "100 First Street", "111-111-1111", "11-111-1111")
    suzy_account = BankAccount("Suzy Que", 3456)
    # suzy_account.deposit(500)
    # suzy_account.withdraw(1000)
    print(suzy_account)

tester()

if __name__ == "__main__":
    tester()