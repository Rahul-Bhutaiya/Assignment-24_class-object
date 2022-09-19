"""
Define a class Employee with instance object variables empid, name, salary. Write
__init__() method in the class to initialize instance object variables. Also define
instance methods to input fields and display field values
"""

class Employee:
    def __init__(self):
        self.empid=int(input('Enter Empid : '))
        self.name=input('Enter Employee Name : ')
        self.salary=int(input('Enter Employee Salary : '))

    def showDetail(self):
        print('Employee Detals ...\nEmpid :',self.empid,'\nEmp_Name :',self.name,'\nEmp_Salary :',self.salary)

obj1=Employee()
obj1.showDetail()