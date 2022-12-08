# list = [15,18,21,24,25,28,30,32,35]
# sum = 0
# for number in list:
#     if number % 5 == 0:
#         sum = sum + number
# print(sum)


# class Employee:
#     def __init__(self,EmployeeName,EmployeeJobTitle,Salary):
#         self.EmployeeName = EmployeeName
#         self.EmployeeJobTitle = EmployeeJobTitle
#         self.Salary = Salary
#
#     def __str__(self):
#         out = str(self.EmployeeName) + " is  an " + str(self.EmployeeJobTitle)
#         out = out + " with a salary of " + str(self.Salary)
#         return out
#
#     def updateSalary(self,Salary):
#         self.Salary = Salary
#
# def tester():
#     emmaLowe = Employee("Emma Lowe", "accountant", 85000)
#     print(emmaLowe)
#     emmaLowe.updateSalary(1000)
#     print(emmaLowe)
#
#
# if __name__ == "__main__":
#    tester()

temp = int(input("What is the temperature"))
if temp <= 32:
    print("Freezing")
elif temp >= 212:
    print("boiling")
else:
    print("ok")
