from  employee import Employee

class Day_base_pay(Employee):
    def __init__(self,emp_name,emp_address,emp_contact,day_pay,days):
        super().__init__(emp_name,emp_address,emp_contact)
        self.day_pay=day_pay
        self.days=days

    def getfullSalary(self):
        return self.day_pay * self.days
