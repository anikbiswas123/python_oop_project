
from  abc import ABC,abstractmethod
#create a class employee

class Employee:
    def __init__(self,emp_name,emp_address,emp_contact):
        self.emp_name=emp_name
        self.emp_address=emp_address
        self.emp_contact=emp_contact

    @property
    def full_info(self):
        return  f"Employe name :{self.emp_name} \t  Address : {self.emp_address} \t  Contact Number : {self.emp_contact}"

    @abstractmethod
    def getfullSalary(self):
        pass

