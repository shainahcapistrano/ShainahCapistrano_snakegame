class Employee:
    def __init__(self, name, job_title, salary):
        self.name = name
        self.job_title = job_title
        self.salary = salary

    @staticmethod
    def update_Salary(new_salary):
        updateSalary = new_salary
        return Employee.updateSalary


def employee_tester():
    emma_jane = Employee("Emma Jane", "accountant", 75000)
    print(emma_jane)
    emma_jane.updateSalary(1000)
    print(emma_jane)

if __name__ == "__main__":
    print()

