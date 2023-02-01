
#create a class payrol

class Payrol:
    def __init__(self):
        self.employee_list=[]

    def add(self,employee):
        self.employee_list.append(employee)

    def show(self):
        for e in self.employee_list:
            print(f"{e.full_info}\t ${e.getfullSalary()}")