#ICP
#This creates a class that will find an employee's avg salary
class Employee:

    def __init__(self):
        self._EmpNum = 0
        self.name = 'Name'
        self.family = 0
        self.salary = 0
        self.department = ''

    def avg_salary(self,years):
        i = years
        total_salary = 0
        while (i > 0):
            avg_s = 0
            salary = int(input("Please enter the employee's salary for year number %d: " % i))
            total_salary = salary + total_salary
            i -= 1
        avg_s = total_salary/years

        return print(avg_s)



#This class inherits the Employee class and asks user to input the employee's info
class Fulltime_Employee (Employee):
    def emp_info(self):
        Fulltime_Employee.name = print(input("Please enter your name: "))
        print(input("Please enter your family size: "))
        print(input("Please enter your current salary: "))
        print(input("Please enter your department name: "))

#These are instances to use the classes from above
emp1 = Employee()
emp1.avg_salary(3)

fe1 = Fulltime_Employee()
fe1.emp_info()
fe1.avg_salary(2)


    


