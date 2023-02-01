
from  fulltime_Employee import  FullTimeEmployee
from  day_base_pay import  Day_base_pay
from  hourly_base_employee import  HourlyBaseEmployee

from payrol import  Payrol

payrol=Payrol()

payrol.add(FullTimeEmployee("sumilon","Dhaka","01764535463",2000))
payrol.add(Day_base_pay("Anika Rahman","mirpur_-1-0","018367455",350,10))
payrol.add(HourlyBaseEmployee("sumiya islam","mohakhalie","01836366464",120,400))
payrol.show()