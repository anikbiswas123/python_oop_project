class user():
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

    def show_detalise(self):
        print("Personal detalises")
        print(" ")
        print(f"user name :{self.name}\n user age :{self.age} \n user gender {self.gender}")

#create child classs
class Bank(user):
    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)
        self.balances = 0

    def deposite(self,amount):
        self.amount=amount
        self.balances += self.amount
        print("Account  balances hase updated BDT",self.balances)

    def withdrew(self,amount):
        self.amount=amount


        if self.amount > self.balances:
            print("Insufficent balances | balanace ",self.balances)

        else:
            self.balances=self.balances - self.amount
            print("Account balances hase update BDT :",self.balances)

    def view_balances(self):
        print("views the total Balances = ",self.balances)


jio=Bank("jio",23,"male")
jio.deposite(800)
jio.deposite(200)
jio.view_balances()
print(" ")
jio.withdrew(500)
jio.view_balances()