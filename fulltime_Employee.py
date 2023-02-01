from  employee import Employee

#create a class fulltimeemployee

class FullTimeEmployee(Employee):
     def __init__(self,emp_name,emp_address,emp_contact,salry):
       super().__init__(emp_name,emp_address,emp_contact)
       self.salary=salry

     def getfullSalary(self):

         return self.salary