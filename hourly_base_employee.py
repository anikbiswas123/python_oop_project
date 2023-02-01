from employee import  Employee

#creata a class

class HourlyBaseEmployee(Employee):
    def __init__(self,emp_name,emp_address,emp_contact,working_hours,rate):
        super().__init__(emp_name,emp_address,emp_contact)
        self.working_hours=working_hours
        self.rate=rate

    def getfullSalary(self):
        return  self.working_hours * self.rate
