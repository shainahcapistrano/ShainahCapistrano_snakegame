
class BankAccount:

    ##Constructor
    def __init__(self, name, account):
         self.owner = name

    ##Class related methods



    ##Nice to have method to print things out
    def __str__(self):
        out = self.owner + " has account " + str(self.account_number)
        out = out + " that contains a balance of " + str(self.balance)
        return out


def tester():
    suzy_account = BankAccount("Suzy Que", 3456)
    print(suzy_account)


if __name__ == "__main__":
    tester()