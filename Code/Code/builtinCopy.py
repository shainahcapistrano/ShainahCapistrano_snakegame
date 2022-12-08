from BankAccount import *
import copy

suzyAcct =  BankAccount("Suzy", 123)
copySuzy = copy.copy(suzyAcct)
suzyAcct.deposit(10)
print(suzyAcct)
print(copySuzy)
